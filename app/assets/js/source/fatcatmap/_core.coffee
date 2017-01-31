## FatCatMap core classes

# setup preinit

if @__fcm_preinit?
    @__fcm_preinit.abstract_base_classes = []
    @__fcm_preinit.abstract_base_controllers = []
    @__fcm_preinit.abstract_base_views = []

else
    @__fcm_preinit =
        abstract_base_classes: []
        abstract_base_controllers: []
        abstract_base_views: []

class Controller extends Model
class View extends Model

class Exception extends Error

    constructor: (@source, @message) ->
    toString: () ->
        return '[' + @source + '] FatCatMap Exception: ' + @message

Util = new window.Util()

@__fcm_preinit.abstract_base_classes.push Exception