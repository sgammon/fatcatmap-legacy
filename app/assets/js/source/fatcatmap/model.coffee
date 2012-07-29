## Native classes
class Person extends Model
    model:
        firstname: String()
        lastname: String()
        names: Array()
        birthdate: Number()
        deathdate: Number()
        nationality: String()
        religion: String()

class Corporation extends Model
class Industry extends Model

## Geo classes
class Nation extends Model
    model:
        fullname: String()
        shortname: String()
        names: Array()

class State extends Model
    model:
        fullname: String()
        shortname: String()
        names: Array()

class City extends Model
    model:
        fullname: String()
        shortname: String()
        names: Array()
        latlong: String()

## Gov't/agency models
class ExecutiveAgency extends Model
class ExecutiveSeat extends Model
class Judiciary extends Model
class Legislature extends Model
class LegislativeHouse extends Model
class LegislativeSeat extends Model
class Committee extends Model

## Law models
class ExecutiveOrder extends Model
class Decision extends Model
class Bill extends Model

## Parliamentary models
class Amendment extends Model
class Rollcall extends Model
class Vote extends Model


@__fcm_preinit.abstract_base_classes.push Person
@__fcm_preinit.abstract_base_classes.push Corporation
@__fcm_preinit.abstract_base_classes.push Nation
@__fcm_preinit.abstract_base_classes.push State
@__fcm_preinit.abstract_base_classes.push City
