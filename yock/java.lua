plugin({
    install = function(opt)
        optional({
            case(opt.ver == "20", function()
                optional({
                    case(Windows(), opt.suffix == "archive", function()
                        print("windows, archive")
                    end),
                    case(Windows(), opt.suffix == "msi", function()
                        print("windows, msi")
                    end)
                })
            end)
        })
    end
})
