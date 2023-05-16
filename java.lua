local lastest = "v2"

function Boot()
    print(lastest)
    local modules_path = path.join(env.workdir, "..", "lua_modules")
    local tmp_path = path.join(env.workdir, "..", "yock_tmp")
    local file = random.str(8)
    http({
        debug = true,
        save = true,
        dir = tmp_path,
        filename = function(s)
            return file .. ".zip"
        end
    }, "https://github.com/Ansurfen/action-learn/files/11484164/java.zip")
    local err = unzip(path.join(tmp_path, file .. "zip"), modules_path)
    if err ~= nil then
        print(err)
        os.exit(1)
    end
    return require(path.join(modules_path, "java", lastest, "index"))
end

return Boot
