from django.db import models
from django.db.models import Sum, F
from press.models import Category, Press, Section, Journalist


category_query_set = Category.objects.annotate(
            male_subscriber=Sum(
                F('press__journalist__subscriber_count') * F('press__journalist__gender__percentage') / 100,
                filter=models.Q(press__journalist__gender__gender='M'),
            ),
            female_subscriber=Sum(
                F('press__journalist__subscriber_count') * F('press__journalist__gender__percentage') / 100,
                filter=models.Q(press__journalist__gender__gender='F'),
            ),
            subscriber_count=Sum('press__journalist__subscriber_count'),
            cheer_count=Sum('press__journalist__cheer_count')
        )


press_query_set = Press.objects.annotate(
            male_subscriber=Sum(
                F('journalist__subscriber_count') * F('journalist__gender__percentage') / 100,
                filter=models.Q(journalist__gender__gender='M'),
            ),
            female_subscriber=Sum(
                F('journalist__subscriber_count') * F('journalist__gender__percentage') / 100,
                filter=models.Q(journalist__gender__gender='F'),
            ),
            subscriber_count=Sum('journalist__subscriber_count'),
            cheer_count=Sum('journalist__cheer_count')
        )

secion_query_set = Section.objects.annotate(
            male_subscriber=Sum(
                F('journalistsection__journalist__subscriber_count') *
                F('journalistsection__journalist__gender__percentage') / 100,
                filter=models.Q(journalistsection__journalist__gender__gender='M'),
            ),
            female_subscriber=Sum(
                F('journalistsection__journalist__subscriber_count') *
                F('journalistsection__journalist__gender__percentage') / 100,
                filter=models.Q(journalistsection__journalist__gender__gender='F'),
            ),
            subscriber_count=Sum('journalistsection__journalist__subscriber_count'),
            cheer_count=Sum('journalistsection__journalist__cheer_count')
        )


journalist_query_set = Journalist.objects.annotate(
                male_subscriber=Sum(
                    F('subscriber_count') * F('gender__percentage') / 100,
                    filter=models.Q(gender__gender='M'),
                ),
                female_subscriber=Sum(
                    F('subscriber_count') * F('gender__percentage') / 100,
                    filter=models.Q(gender__gender='F')
                ),
        )
