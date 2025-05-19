from ..utils.database import ma
from ..models.booking import Booking


class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True
        include_fk = True
        fields = (
            "salon_name", "salon_id", "booking_time", "salon_address", "salons_city", "service_name", "service_id",
            "master_name",
            "master_id", "status")

    salon_name = ma.Function(lambda obj: obj.salon.name if obj.salon.name else None)
    salon_address = ma.Function(lambda obj: obj.salon.street_address if obj.salon.name else " ")
    salons_city = ma.Function(lambda obj: obj.salon.city.name if obj.salon.city.name else " ")
    service_name = ma.Function(lambda obj: obj.service.service_name.name if obj.service.service_name.name else None)
    master_name = ma.Function(lambda obj: obj.master.full_name if obj.master.full_name else None)
