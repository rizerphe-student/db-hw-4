import csv
from dataclasses import dataclass
from datetime import datetime
import random

from .generate_characteristics import BusType, filtered_bus_types


def random_name() -> str:
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10)).capitalize()


def random_date() -> datetime:
    return datetime.now()


def random_bool() -> bool:
    return random.choice([True, False])


def random_int() -> int:
    return random.randint(0, 10000000)


def random_string() -> str:
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10))


def random_coordinates() -> str:
    return f"{random_int()};{random_int()}"


def random_license_plate() -> str:
    return (
        "".join(random.choices("AB", k=2))
        + "".join(random.choices("0123456789", k=4))
        + "".join(random.choices("AB", k=2))
    )


def random_route_no() -> int:
    return random.randint(0, 10000000)


def random_model_id() -> int:
    return random.randint(0, 10000000)


def random_passenger_id() -> int:
    return random.randint(0, 10000000)


def random_stop_order() -> int:
    return random.randint(0, 10000000)


@dataclass
class DriverData:
    licenseID: int
    name_firstName: str
    name_lastName: str

    @staticmethod
    def random() -> "DriverData":
        return DriverData(
            licenseID=random_int(),
            name_firstName=random_name(),
            name_lastName=random_name(),
        )


@dataclass
class BusData:
    licensePlate: str
    characteristics_model_id: int
    working: int

    @staticmethod
    def random(characteristics_model_id: int) -> "BusData":
        return BusData(
            licensePlate=random_license_plate(),
            characteristics_model_id=characteristics_model_id,
            working=1 if random_bool() else 0,
        )


@dataclass
class RouteData:
    routeNo: int

    @staticmethod
    def random() -> "RouteData":
        return RouteData(routeNo=random_route_no())


@dataclass
class StopData:
    stopID: int
    stopName: str
    stopCoordinates: str

    @staticmethod
    def random() -> "StopData":
        return StopData(
            stopID=random_int(),
            stopName=random_name(),
            stopCoordinates=random_coordinates(),
        )


@dataclass
class RideData:
    rideID: int
    licensePlate: str
    routeNo: int
    licenseID: int
    startTime: datetime

    @staticmethod
    def random(licensePlate: str, routeNo: int, licenseID: int) -> "RideData":
        return RideData(
            rideID=random_int(),
            licensePlate=licensePlate,
            routeNo=routeNo,
            licenseID=licenseID,
            startTime=random_date(),
        )


@dataclass
class TicketUseData:
    useID: int
    rideID: int
    w_ticketID: int | None
    o_ticketID: int | None

    @staticmethod
    def random(w_ticketID: int | None, o_ticketID: int | None) -> "TicketUseData":
        # Only one of the two can be set
        o_ticketID = o_ticketID if w_ticketID is None else None

        return TicketUseData(
            useID=random_int(),
            rideID=random_int(),
            w_ticketID=w_ticketID,
            o_ticketID=o_ticketID,
        )


@dataclass
class OneTimeTicketData:
    ticketID: int
    issueDate: datetime
    passengerID: int

    @staticmethod
    def random(passengerID: int) -> "OneTimeTicketData":
        return OneTimeTicketData(
            ticketID=random_int(), issueDate=random_date(), passengerID=passengerID
        )


@dataclass
class WeeklyTicketData:
    ticketID: int
    issueDate: datetime
    passengerID: int

    @staticmethod
    def random(passengerID: int) -> "WeeklyTicketData":
        return WeeklyTicketData(
            ticketID=random_int(), issueDate=random_date(), passengerID=passengerID
        )


@dataclass
class PassengerData:
    passengerID: int
    name_firstName: str
    name_lastName: str

    @staticmethod
    def random() -> "PassengerData":
        return PassengerData(
            passengerID=random_passenger_id(),
            name_firstName=random_name(),
            name_lastName=random_name(),
        )


@dataclass
class BusCharacteristicsData:
    model_id: int
    name: str
    size: int
    description: str

    @staticmethod
    def from_data(data: BusType) -> "BusCharacteristicsData":
        return BusCharacteristicsData(
            model_id=random_model_id(),
            name=data.name,
            size=100,
            description=data.full_text,
        )


@dataclass
class StopEnRouteData:
    stopID: int
    routeID: int
    stopOrder: int

    @staticmethod
    def random(stopID: int, routeID: int) -> "StopEnRouteData":
        return StopEnRouteData(
            stopID=stopID, routeID=routeID, stopOrder=random_stop_order()
        )


def populate():
    drivers = [DriverData.random() for _ in range(10)]
    bus_characteristics = [
        BusCharacteristicsData.from_data(bus) for bus in filtered_bus_types
    ]
    buses = [
        BusData.random(random.choice(bus_characteristics).model_id) for _ in range(10)
    ]
    routes = [RouteData.random() for _ in range(10)]
    stops = [StopData.random() for _ in range(10)]
    rides = [
        RideData.random(
            random.choice(buses).licensePlate,
            random.choice(routes).routeNo,
            random.choice(drivers).licenseID,
        )
        for _ in range(10)
    ]
    passengers = [PassengerData.random() for _ in range(10)]
    stops_en_route = [
        StopEnRouteData.random(
            random.choice(stops).stopID, random.choice(routes).routeNo
        )
    ]
    # Do we really need these?
    one_time_tickets = []
    weekly_tickets = []
    ticket_uses = []

    # Now, we need to write all of this to the relevant csv files
    with open("data/drivers.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DriverData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([driver.__dict__ for driver in drivers])
    with open("data/bus_characteristics.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=BusCharacteristicsData.__annotations__.keys()
        )
        writer.writeheader()
        writer.writerows(
            [characteristics.__dict__ for characteristics in bus_characteristics]
        )
    with open("data/buses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=BusData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([bus.__dict__ for bus in buses])
    with open("data/routes.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=RouteData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([route.__dict__ for route in routes])
    with open("data/stops.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=StopData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([stop.__dict__ for stop in stops])
    with open("data/rides.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=RideData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([ride.__dict__ for ride in rides])
    with open("data/passengers.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=PassengerData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([passenger.__dict__ for passenger in passengers])
    with open("data/stops_en_route.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=StopEnRouteData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([stop.__dict__ for stop in stops_en_route])
    with open("data/one_time_tickets.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=OneTimeTicketData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([ticket.__dict__ for ticket in one_time_tickets])
    with open("data/weekly_tickets.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=WeeklyTicketData.__annotations__.keys())
        writer.writeheader()
        writer.writerows([ticket.__dict__ for ticket in weekly_tickets])
    with open("data/ticket_uses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TicketUseData.__annotations__.keys())
        writer.writeheader()
        writer.writerows(ticket_uses)


if __name__ == "__main__":
    random.seed(0)
    populate()
