driver(function(opt, ...)
    table.dump(opt)
    for _, value in ipairs({ ... }) do
        print(value)
    end
end)
