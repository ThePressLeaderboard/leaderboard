from django.db import models
from django.db.models import F, Sum

from press.models import Category, Journalist, Press, Section

category_query_set = Category.objects.annotate(
    male_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__gender__percentage")
        / (100*6),
        filter=models.Q(press__journalist__gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__gender__percentage")
        / (100*6),
        filter=models.Q(press__journalist__gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100*2),
        filter=models.Q(press__journalist__age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100*2),
        filter=models.Q(press__journalist__age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100*2),
        filter=models.Q(press__journalist__age__age="30"),
    ),
    forty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100*2),
        filter=models.Q(press__journalist__age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100*2),
        filter=models.Q(press__journalist__age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100*2),
        filter=models.Q(press__journalist__age__age="60"),
    ),
    subscriber_count=Sum("press__journalist__subscriber_count")/12,
    cheer_count=Sum("press__journalist__cheer_count")/12,
)


press_query_set = Press.objects.annotate(
    male_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__gender__percentage") / (100*6),
        filter=models.Q(journalist__gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__gender__percentage") / (100*6),
        filter=models.Q(journalist__gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__age__percentage") / (100*2),
        filter=models.Q(journalist__age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__age__percentage") / (100*2),
        filter=models.Q(journalist__age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__age__percentage") / (100*2),
        filter=models.Q(journalist__age__age="30"),
    ),
    forty_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__age__percentage") / (100*2),
        filter=models.Q(journalist__age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__age__percentage") / (100*2),
        filter=models.Q(journalist__age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("journalist__subscriber_count") * F("journalist__age__percentage") / (100*2),
        filter=models.Q(journalist__age__age="60"),
    ),
    subscriber_count=Sum("journalist__subscriber_count")/12,
    cheer_count=Sum("journalist__cheer_count")/12,
)

secion_query_set = Section.objects.annotate(
    male_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__gender__percentage")
        / (100*6),
        filter=models.Q(journalistsection__journalist__gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__gender__percentage")
        / (100*6),
        filter=models.Q(journalistsection__journalist__gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100*2),
        filter=models.Q(journalistsection__journalist__age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100*2),
        filter=models.Q(journalistsection__journalist__age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100*2),
        filter=models.Q(journalistsection__journalist__age__age="30"),
    ),
    forty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100*2),
        filter=models.Q(journalistsection__journalist__age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100*2),
        filter=models.Q(journalistsection__journalist__age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100*2),
        filter=models.Q(journalistsection__journalist__age__age="60"),
    ),
    subscriber_count=Sum("journalistsection__journalist__subscriber_count")/12,
    cheer_count=Sum("journalistsection__journalist__cheer_count")/12,
)


journalist_query_set = Journalist.objects.annotate(
    male_subscriber=Sum(
        F("subscriber_count") * F("gender__percentage") / (100*6),
        filter=models.Q(gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("subscriber_count") * F("gender__percentage") / (100*6),
        filter=models.Q(gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100*2),
        filter=models.Q(age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100*2),
        filter=models.Q(age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100*2),
        filter=models.Q(age__age="30"),
    ),
    forty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100*2),
        filter=models.Q(age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100*2),
        filter=models.Q(age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100*2),
        filter=models.Q(age__age="60"),
    ),
)
