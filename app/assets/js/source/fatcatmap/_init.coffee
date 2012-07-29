## FatCatMap system init
class FatCatMap

    constructor: (window) ->

        @sys = 

            core_events: ['FATCATMAP_READY']        # for use in init

            # internal state
            state:
                status: 'NOT_READY'
                flags: []
                preinit: {}
                controllers: {}
                classes: {}
                views: {}

                consider_preinit: (preinit) =>
                    @sys.preinit = preinit

                    for k, kind of preinit
                        for base_obj in kind if kind?
                            @sys.install(base_obj)

                    return preinit

                sniff_headers: (document) =>
                    $.apptools.dev.verbose('fcm', 'You can\'t smell any cookies, you haven\'t written yourself a nose!')
                    return

            install: (obj) =>
                sys_mount = false

                if obj.mount?
                    # it's a controller
                    sys_mount = true
                    mount_point = obj.mount
                    @sys.state.controllers[mount_point] = obj
                else
                    # for now handle views & classes the same
                    mount_point = obj.constructor.name
                    @sys.state.classes[mount_point] = obj

                if obj.events?
                    $.apptools.events.register(event) for event in obj.events

                obj = new obj(@, window)

                if not obj.export? or obj.export is 'public'
                    window[mount_point] = obj
                    
                if sys_mount
                    @[mount_point] = obj

                obj._init?()
                return obj

            go: () =>
                @sys.state.status = 'READY'
                $.apptools.events.trigger('FATCATMAP_READY')
                $.apptools.dev.verbose('fcm', 'FatCatMap systems go.')
                return @

        if window.__fcm_preinit?
            @sys.state.consider_preinit(window.__fcm_preinit)

        return @sys.go()

window.FatCatMap = FatCatMap
window.fatcatmap = new FatCatMap(window)

if $?
    $.extend fatcatmap: window.FatCatMap

else
    window.$ = (id) -> return if Util? then Util.get(id) else document.getElementById(id)
    window.$.openfire = window.openfire