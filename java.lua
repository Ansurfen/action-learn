local lastest = "v2"

function Boot()
    print(lastest)
    local modules_path = path.join(env.workdir, "..", "lua_modules")
    local tmp_path = path.join(env.workdir, "..", "yock_tmp")
    local url = "https://github.com/Ansurfen/action-learn/files/11484164/java.zip"
    local file = y:get_cache(url)
    if type(file) == "string" and #file > 0 then

    else
        file = random.str(8)
        yassert(http({
            debug = true,
            save = true,
            dir = tmp_path,
            filename = function(s)
                return file .. ".zip"
            end
        }, url))
        y:set_cache(url, file)
    end
    yassert(unzip(path.join(tmp_path, file .. ".zip"), path.join(modules_path, "java")))
    return require(path.join(modules_path, "java", lastest, "index"))
end

return Boot
