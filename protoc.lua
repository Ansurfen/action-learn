local lastest = "v1"

function Boot(module)
    local modules_path = path.join(env.workdir, "..", "lua_modules")
    local tmp_path = path.join(env.workdir, "..", "yock_tmp")
    local url = "https://github.com/Ansurfen/action-learn/files/11521499/protoc.zip"
    local file = fetch.zip(url)
    yassert(unzip(path.join(tmp_path, file .. ".zip"), path.join(modules_path, module)))
    ypm:new_module(module, lastest)
    return require(path.join(modules_path, module, lastest, "index"))
end

return Boot
