from django.db import models
from uuid import uuid4

class Titan(models.Model):
    ELDIA = 'eldia'
    MARLEY = 'marley'

    ALLEGIANCE_CHOISES = [
        (ELDIA, 'Eldia'),
        (MARLEY, 'Marley')
    ];

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    other_names = models.CharField(max_length=200, null=True)
    abilities = models.CharField(max_length=200)
    allegiance = models.CharField(
        choices=ALLEGIANCE_CHOISES,
        default=MARLEY,
        max_length=10
    )

    def __str__(self) -> str:
        return self.name;

# Create your models here.
class Character(models.Model):
    ALIVE = 'alive'
    DECEASED = 'deceased'
    UNKNOWN = 'unknown'

    STATUS_CHOISES = [
        (ALIVE, 'Alive'),
        (DECEASED, 'Deceased'),
        (UNKNOWN, 'Unknown')
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    spices = models.CharField(max_length=200)
    height = models.IntegerField(null=True)
    residence = models.CharField(max_length=200)
    status = models.CharField(
        choices=STATUS_CHOISES,
        default=UNKNOWN,
        max_length=20
    )
    alias = models.CharField(max_length=200, null=True)
    titan = models.OneToOneField(to=Titan, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)

    def isTeenager (self) -> bool:
        return self.age < 20