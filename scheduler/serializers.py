from rest_framework import serializers

from .models import Event, People, TesterSection, Tester, Customer, Device


# Serializers help to format data that is sent between django and other components. In this case it is recieving the
# data sent by the scheduler javascript and formatting it as we tell it to so that django can easily send it to the
# database.

# Serializer for the 'Event' model
class EventSerializer(serializers.ModelSerializer):
    # Custom date and time formatting for start_date and end_date fields
    start_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    end_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Event
        # Define fields to include in the serialized representation of the 'Event' model
        fields = ('id', 'text', 'start_date', 'end_date', 'tester', 'person', 'customer', 'job_number',
                  'device', 'description', 'locked', 'window_lot', 'number_units', 'department', 'steps',
                  'peripherals', 'test_temps')


# Serializer for the 'People' model
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        # Define fields to include in the serialized representation of the 'People' model
        fields = ('key', 'label', 'role')


# Serializer for the 'TesterSection' model, this is used to group testers together for the dropdown in the scheduler
class TesterSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesterSection
        fields = ('key', 'label', 'open')


# Serializer for the 'Tester' model
class TesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tester
        fields = ('key', 'label')


# Serializer for the 'Customer' model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('key', 'label')


# Serializer for the 'Device' model
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('key', 'label')
