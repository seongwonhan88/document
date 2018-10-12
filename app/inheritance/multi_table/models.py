from django.db import models


class Place1(models.Model):

    # id = models.Autofield(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name} [Place]'

    class Meta:
        db_table = "Inheritance_Multitable_Place"

def get_removed_place():
    try:
        place = Place1.objects.get(name='철거됨')
    except Place1.DoesNotExist:
        place = Place1.objects.create(name='철거됨')
    return place

class Restaurant1(Place1):
    # Multitable inheritance 구현 시 암시적으로 생성되는 one to one 필드
    # 부모 클래스의 소문자화_ptr models.onetoonefield(<부모클래스>)
    # place1_ptr = models.one to one(place1, primary_key=True)
    # 임이의 필드에 parent_link = True 옵션을 주면 <부모클래스의 소문자>_ptr 필드가 생성되지 않음

    # place_ptr = models.OneToOneField(Place, parent_link=True, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    old_place = models.ForeignKey(
        Place1, verbose_name='이전 가게 주소',
        blank=True,
        null=True,
        # 만약에 주소건물이 없어졌을 경우 , default 값을 담다
        # 위와 같은 정보를 담고 있는 Place1 객체가 필요(DB row) 가 필요
        # SET 의 함수가 해당 DB row 데이터를 가져오거나 생성하게 함
        on_delete=models.SET(get_removed_place),
        related_query_name='old_restaurant',
        related_name='old_restaurants'
    )

    def __str__(self):
        return f'{self.name} [Restaurant]'

    class Meta:
        db_table = "Inheritance_Multitable_Restaurant"