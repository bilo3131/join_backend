from datetime import datetime
from rest_framework import serializers
from join_app.models import Contact, Task, Category, Subtasks


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = "__all__"

class SubtaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtasks
        fields = ["id", "title", "completed"]
        
class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    assignees = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True)
    date = serializers.DateField(
        input_formats=["%d.%m.%Y", "%Y-%m-%d"],
        format="%Y-%m-%d"
    )

    class Meta:
        model = Task
        fields = "__all__"
        
    def create(self, validated_data):
    # Subtasks aus den Daten extrahieren
        subtask_data = validated_data.pop('subtasks', [])
        assignees_data = validated_data.pop('assignees', [])

        task = Task.objects.create(**validated_data)

        # Subtasks erstellen
        for subtask in subtask_data:
            subtask_instance = Subtasks.objects.create(**subtask)
            task.subtasks.add(subtask_instance)

        # Assignees zuweisen
        task.assignees.set(assignees_data)  # Assignees setzen, statt direkte Zuweisung

        return task
    
    def update(self, instance, validated_data):
    # Subtasks aktualisieren
        subtask_data = validated_data.pop('subtasks', [])
        instance = super().update(instance, validated_data)

        # Bestehende Subtasks synchronisieren
        current_subtask_ids = {subtask.id for subtask in instance.subtasks.all()}
        new_subtask_ids = set()

        for subtask in subtask_data:
            subtask_instance, created = Subtasks.objects.update_or_create(
                id=subtask.get('id'),
                defaults=subtask
            )
            new_subtask_ids.add(subtask_instance.id)

        # Entferne Subtasks, die nicht mehr im Update enthalten sind
        instance.subtasks.set(Subtasks.objects.filter(id__in=new_subtask_ids))
        return instance

    def validate_date(self, value):
        """
        Zusätzliche Validierung für das Datum, z. B. kein Datum in der Vergangenheit zulassen.
        """
        if value < datetime.today().date():
            raise serializers.ValidationError("Das Datum darf nicht in der Vergangenheit liegen.")
        return value

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"