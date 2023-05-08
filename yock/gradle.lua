plugin({
    install = function ()
        print("准备安装gradle,检测java是否存在")
        pull({
            plugins = {
                "yock/java"
            }
        })
        local _plugin = gdns:GetPlugin("yock/java")
        if _plugin.Path ~= "" then
            load_plugin(pathf("@/plugin/") .. _plugin.Path.Path .. ".lua")
        end
    end
})