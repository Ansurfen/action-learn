driver(function(opt, ...)
    if opt ~= nil and opt.plugins ~= nil then
        pull({ plugins = opt.plugins })
        for _, plugin in ipairs(opt.plugins) do
            if ldns:GetPlugin(plugin).URL ~= "" then
                local uid = load_plugin(pathf("@/plugin/") .. ldns:GetPlugin(plugin).Path .. ".lua")
                plugins[uid].install()
            end
            if gdns:GetPlugin(plugin).URL ~= "" then
                load_plugin(pathf("@/plugin/") .. gdns:GetPlugin(plugin).Path .. ".lua")
            end
        end
    end
end)
