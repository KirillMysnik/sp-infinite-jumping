from cvars.public import PublicConVar
from plugins.info import PluginInfo


info = PluginInfo()
info.name = "Infinite Jumping"
info.basename = 'infinite_jumping'
info.author = 'Kirill "iPlayer" Mysnik'
info.version = '1.0.1'
info.variable = "ij_version"
info.convar = PublicConVar(
    info.variable, info.version, "{} version".format(info.name))

info.url = "https://github.com/KirillMysnik/sp-infinite-jumping"
