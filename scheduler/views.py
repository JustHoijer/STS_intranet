from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from scheduler.serializers import (
    EventSerializer,
    PeopleSerializer,
    TesterSerializer,
    CustomerSerializer,
    DeviceSerializer,
)

from .models import Event, People, TesterSection, Tester, Customer, Device


# Helper function to retrieve children of a TesterSection recursively
def getChildren(section):
    children = []
    if section.testerselections.all():
        for child_section in section.testerselections.all().order_by("priority"):
            child_children = getChildren(child_section)
            children.append(
                {
                    "key": child_section.keyTesterSection,
                    "label": child_section.label,
                    "open": child_section.open,
                    "children": child_children,
                }
            )
    if section.testers.all():
        for tester in section.testers.all().order_by("priority"):
            children.append({"key": tester.key, "label": tester.label})
    return children


# Helper function to build sections hierarchy
def buildSections():
    sections = []
    sectionslist = TesterSection.objects.filter(parent=None).order_by("priority")
    for section in sectionslist:
        children = getChildren(section)
        sections.append(
            {
                "key": section.keyTesterSection,
                "label": section.label,
                "open": section.open,
                "children": children,
            }
        )
    return sections


# View for rendering the main index page
def index(request):
    return render(request, "scheduler/index.html")


# API view for listing and adding data
@api_view(["GET", "POST"])
def data_list(request, offset):
    if request.method == "GET":
        from_date = request.GET.get("from")
        to_date = request.GET.get("to")

        # Serialize data from People, Tester, Customer, and Device models
        peopleData = PeopleSerializer(People.objects.all(), many=True)
        testerData = TesterSerializer(Tester.objects.all(), many=True)
        customerData = CustomerSerializer(Customer.objects.all(), many=True)
        deviceData = DeviceSerializer(Device.objects.all(), many=True)

        # Build the hierarchy of sections
        sections = buildSections()

        collections = {
            "people": peopleData.data,
            "testerslist": testerData.data,
            "customers": customerData.data,
            "devices": deviceData.data,
            "sections": sections,
        }
        if from_date and to_date:
            # Filter events based on date range
            events = Event.objects.filter(
                start_date__lt=to_date, end_date__gte=from_date
            )
            if events:
                # Serialize event data if events exist within the date range
                eventsData = EventSerializer(events, many=True)
                print("There are Events!")

                return Response(
                    {
                        "data": eventsData.data,
                        # 'user_authenticated': request.user.is_authenticated
                        "collections": collections,
                    }
                )
            print("No Events!")
        return Response({"collections": collections})

    elif request.method == "POST":
        # Handle adding new events
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            event = serializer.save()
            return JsonResponse({"action": "inserted", "tid": event.id})
        print("hello dummy 1")
        return JsonResponse({"action": "error"})


# API view for updating and deleting events
@api_view(["PUT", "DELETE"])
def event_update(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return JsonResponse({"action": "error2"})

    # Handle updating events
    if request.method == "PUT":
        serializer = EventSerializer(event, data=request.data)
        # print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"action": "updated"})
        return JsonResponse({"action": "error"})

    # Handle deleting events
    if request.method == "DELETE":
        event.delete()
        return JsonResponse({"action": "deleted"})


# View for checking event date overlaps
def data_check(request):
    if request.method == "GET":
        startDate = request.GET.get("start_date", None)
        endDate = request.GET.get("end_date", None)
        tester = request.GET.get("tester", None)
        eventID = request.GET.get("id", None)

        # Check for overlapping events for the same tester
        overlapping = Event.objects.filter(
            tester=tester,
            start_date__lt=endDate,
            end_date__gt=startDate,
        ).exclude(id=eventID)
        if overlapping.exists():
            return JsonResponse({"is_allowed": False})
        else:
            return JsonResponse({"is_allowed": True})
    return
