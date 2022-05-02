from django.db import models

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

    def __str__(self) -> str:
        return self.first_name

    def isTeenager (self) -> bool:
        return self.age < 20