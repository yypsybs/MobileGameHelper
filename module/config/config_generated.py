import datetime

# This file was automatically generated by module/config/config_updater.py.
# Don't modify it manually.


class GeneratedConfig:
    """
    Auto generated configuration
    """

    # Group `Scheduler`
    Scheduler_Enable = False
    Scheduler_NextRun = datetime.datetime(2020, 1, 1, 0, 0)
    Scheduler_Command = 'Alas'
    Scheduler_ServerUpdate = '04:00'

    # Group `Emulator`
    Emulator_Serial = 'auto'
    Emulator_PackageName = 'auto'  # auto, com.YostarJP.BlueArchive, com.hypergryph.arknights, com.hypergryph.arknights.bilibili, com.bilibili.priconne
    Emulator_ScreenshotMethod = 'auto'  # auto, ADB, ADB_nc, uiautomator2, aScreenCap, aScreenCap_nc, DroidCast, DroidCast_raw, scrcpy
    Emulator_ControlMethod = 'MaaTouch'  # minitouch, MaaTouch
    Emulator_AdbRestart = False

    # Group `EmulatorInfo`
    EmulatorInfo_Emulator = 'auto'  # auto, NoxPlayer, NoxPlayer64, BlueStacks4, BlueStacks5, BlueStacks4HyperV, BlueStacks5HyperV, LDPlayer3, LDPlayer4, LDPlayer9, MuMuPlayer, MuMuPlayerX, MuMuPlayer12, MEmuPlayer
    EmulatorInfo_name = None
    EmulatorInfo_path = None

    # Group `Error`
    Error_Restart = 'game'  # game, game_emulator
    Error_SaveError = True
    Error_ScreenshotLength = 1
    Error_OnePushConfig = 'provider: null'

    # Group `Optimization`
    Optimization_ScreenshotInterval = 0.3
    Optimization_CombatScreenshotInterval = 1.0
    Optimization_WhenTaskQueueEmpty = 'goto_main'  # stay_there, goto_main, close_game

    # Group `JumpTo`
    JumpTo_ConfigName = 'null'
