from press.models import Press


def test_press_model(db):
    # pytest, pytest-django
    press_sample = Press.objects.create(press_id="123", name="조선일보")

    assert Press.objects.count() == 1
