plugin({
    install = function()
        print("准备安装fabric,检测gralde是否存在")
        pull({
            plugins = {
                "yock/gradle"
            }
        })
        local _plugin = gdns:GetPlugin("yock/gradle")
        if _plugin.Path ~= "" then
            local uid = load_plugin(pathf("@/plugin/") .. _plugin.Path .. ".lua")
            plugins[uid].install()
        end
    end
})
