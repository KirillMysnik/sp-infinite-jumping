from entities.constants import MoveType
from entities.hooks import EntityCondition, EntityPreHook
from memory import make_object
from players import UserCmd
from players.constants import PlayerButtons, PlayerStates
from players.entity import Player


from .info import info


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
