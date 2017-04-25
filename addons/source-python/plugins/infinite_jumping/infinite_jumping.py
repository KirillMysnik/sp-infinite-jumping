# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from cvars import ConVar
from entities.constants import MoveType
from entities.hooks import EntityCondition, EntityPreHook
from memory import make_object
from players import UserCmd
from players.constants import PlayerButtons, PlayerStates
from players.entity import Player


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
AIR_ACCELERATE = 9999

cvar_enablebunnyhopping = ConVar("sv_enablebunnyhopping")
cvar_airaccelerate = ConVar("sv_airaccelerate")

old_cvar_value_enablebunnyhopping = None
old_cvar_value_airaccelerate = None


# =============================================================================
# >> HOOKS
# =============================================================================
@EntityPreHook(EntityCondition.is_human_player, 'run_command')
def pre_run_command(args):
    player = make_object(Player, args[0])

    # Is player dead?
    if player.dead:
        return

    # Is player on ladder?
    if player.move_type & MoveType.LADDER:
        return

    # Is player in water deep enough?
    if player.get_property_uchar('m_nWaterLevel') > 1:
        return

    # Is player already on ground?
    if player.flags & PlayerStates.ONGROUND:
        return

    user_cmd = make_object(UserCmd, args[1])
    user_cmd.buttons &= ~PlayerButtons.JUMP


# =============================================================================
# >> LOAD & UNLOAD FUNCTIONS
# =============================================================================
def load():
    global old_cvar_value_enablebunnyhopping, old_cvar_value_airaccelerate
    old_cvar_value_enablebunnyhopping = cvar_enablebunnyhopping.get_bool()
    old_cvar_value_airaccelerate = cvar_airaccelerate.get_int()

    cvar_enablebunnyhopping.set_bool(True)
    cvar_airaccelerate.set_int(AIR_ACCELERATE)


def unload():
    cvar_enablebunnyhopping.set_bool(old_cvar_value_enablebunnyhopping)
    cvar_airaccelerate.set_int(old_cvar_value_airaccelerate)
