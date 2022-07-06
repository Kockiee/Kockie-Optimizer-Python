from tkinter import *
from tkinter import filedialog as dlg
from tkinter import ttk
from ttkthemes import ThemedTk
from time import sleep
from PIL import ImageTk, Image
import shutil
import webbrowser
import tkinter as tk
import emoji
import os
import ctypes

if not ctypes.windll.shell32.IsUserAnAdmin():
    import sys
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)

varWin = []
user = str(os.getlogin())

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def btn1Action():
    try:
        os.startfile(r"files\OW.bat")
        sleep(4)
        tk.messagebox.showinfo('Operação Concluída', 'Seu Windows foi otimizado !\n :)')
    except:
        tk.messagebox.showerror('Error', 'O arquivo OW.bat não existe ou está no diretório incorreto !\n :(')

def btn3Action():
    try:
        os.startfile(r"files\RA.bat")
        tk.messagebox.showinfo('Operação Concluída', 'Apps excluídos !\n :)')
    except:
        tk.messagebox.showerror('Erro', 'Algo deu errado !\n :(')

def btn4Action():
    try:
        os.startfile(r"files\AI.bat")
        tk.messagebox.showinfo('Operação Concluída', 'Apps/Drivers instalados com sucesso !\n :)')
    except:
        tk.messagebox.showerror('Erro', 'Algo deu errado !\n :(')

def btn5Action():
    webbrowser.open('https://www.youtube.com/channel/UCYLoDNZ_JOE_W1LFkSTLWpQ')

def btn6Action():
    webbrowser.open('https://discord.gg/g6NkdMSVFA')

def btn2Action():
    varchk = IntVar()

    def btnFortniteAction():
        try:
            if varchk.get() == 0:
                with open(fr'C:\Users\{user}\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini', 'w+') as file:
                    file.write(
                        "[/Script/FortniteGame.FortGameUserSettings]\n"
                        "FullscreenMode=1\n"
                        "UnlockConsoleFPS=False\n"
                        "SubGameSelectCount_Athena=18\n"
                        "SubGameLastSelectedTime_Athena=2021.11.19-14.20.26\n"
                        "SubGameSelectCount_Campaign=0\n"
                        "SubGameLastSelectedTime_Campaign=0001.01.01-00.00.00\n"
                        "LastTimeSettingsSnapshotUploaded=2021.11.19-17.02.48\n"
                        "FirstLoginOnDevice=2021.09.23-10.47.07\n"
                        "SafeZone=1.000000\n"
                        "bIsSafeZoneSet=False\n"
                        "CachedPlayerLevel=59\n"
                        "bShowActorsWithSeasonItemTagMapIndicators=True\n"
                        "CachedBattleStars=0\n"
                        "CachedAlienStylePoints=0\n"
                        "CachedStylePoints=0\n"
                        'CachedClaimableRewards=(("Reward", 68),("Customization", 12))\n'
                        "CachedHighestBattlePassUnlockedPage=1\n"
                        "bShowCareerTabBang=True\n"
                        "FrontendQuestTooltipDisplayedCount=2\n"
                        "CustomVoiceChatInputDevice=\n"
                        "CustomVoiceChatOutputDevice=\n"
                        "CustomVoiceChatInputDeviceId=\n"
                        "CustomVoiceChatOutputDeviceId=\n"
                        "bMotionBlur=False\n"
                        "bShowGrass=False\n"
                        "bShowFPS=True\n"
                        "bUseGPUCrashDebugging=False\n"
                        "bLatencyTweak1=False\n"
                        "LatencyTweak2=1\n"
                        "bLatencyFlash=False\n"
                        "DLSSQuality=0\n"
                        "bRayTracing=False\n"
                        "RayTracingShadowsQuality=True\n"
                        "RayTracingReflectionsQuality=0\n"
                        "RayTracingAmbientOcclusionQuality=True\n"
                        "RayTracingAOQuality=0\n"
                        "RayTracingGIQuality=0\n"
                        "b120FpsMode=False\n"
                        "DisplayGamma=2.200000\n"
                        "UserInterfaceContrast=1.000000\n"
                        "NamedTimes=()\n"
                        'NamedCounts=(("lastfrontendflow_Fortnite", 18),("lastfrontendflow_Fortnite_HotfixVer", 0),("Cube_Queen_Cinematic", 18),("Cube_Queen_Cinematic_HotfixVer", 0),("FNmares_Ariana_Emote", 18),("FNmares_Ariana_Emote_HotfixVer", 0),("STARS_Team_intro", 18),("STARS_Team_intro_HotfixVer", 0),("November_Crew", 18),("November_Crew_HotfixVer", 0),("Jinx_Video", 18),("Jinx_Video_HotfixVer", 0),("DiscoveryLobbyMatchmakingPlay", 18),("DiscoveryLobbyMatchmakingPlay_HotfixVer", 0),("Naruto_Cinematic", 18),("Naruto_Cinematic_HotfixVer", 0),("BRUTE_War_Effort", 18),("BRUTE_War_Effort_HotfixVer", 0),("UEnableMultiFactorModal::ShouldShowMFASplashScreen", 18),("UEnableMultiFactorModal::ShouldShowMFASplashScreen_HotfixVer", 0),("FrontendContext:ShouldShowSocialImport", 18),("FrontendContext:ShouldShowSocialImport_HotfixVer", 0)\n)'
                        'BattlePassOverrideTracker=0\n'
                        'CrewBlingItemShopViolatorUnlockedStagesWhenDisplayed=0\n'
                        "bHasSeenCrewBlingTabBangs=False\n"
                        "bHasSeenDonutShopSequence=False\n"
                        "DonutIdleGameHighScore=0.000000\n"
                        'DisplayAssetPathToOfferSeenLevel=(("v2:/f9e24b8d4b7ab325a4487729d9cf969c750f859a95c7a690de20f79b8df82822", ItemShopVisited),("v2:/8f22f5b37116fd357b6192af46714995ff7d12ea6157980d2d075453c0426492", ItemShopVisited),("v2:/1023f2d8d0984911e2fe3a1fdf23b70a7218189b411bca81a0e493abd5b59677", ItemShopVisited),("v2:/83c2c7dd1240222394ed9c7415fbce183d8504842eebc30039ce96c929d365e6", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_AngelDarkStarterPack.DAv2_RMT_AngelDarkStarterPack", OfferSectionVisited),("v2:/22810a78f6e6f0ede3fdd932101b41347c895a519851438f40bc4f6aa4361bf0", ItemShopVisited),("v2:/3123175e86a2eb2e7e2c0142d72bbee17e21e5e02326d7b12e00280498ddb18a", ItemShopVisited),("v2:/e789e06787eca79f4102ef909578d7696798e148d0550c775e79a61ab4a35a2e", ItemShopVisited),("v2:/222374fc7ea9f6ef8eb0b3c20f3a5d7f64f612e9f3435c74e3d51d785739bf9f", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MagmaMasters.DAv2_RMT_MagmaMasters", OfferSectionVisited),("v2:/570ff3bed6fc8a1f7006610dbb6ce9e4bcd244a32caa435a60392460da356c88", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MaskedDancer.DAv2_RMT_MaskedDancer", ItemShopVisited),("v2:/6633ab8087f2a2e80bdf7a90d06351e7a03b82790cc2e286f4b6851020532ed4", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack1000.DA_MtxPack1000", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack2800.DA_MtxPack2800", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_Featured_LarsBundle.DA_Featured_LarsBundle", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack5000.DA_MtxPack5000", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack13500.DA_MtxPack13500", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season11_BattlePass.DA_BR_Season11_BattlePass", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season18_BattlePass.DA_BR_Season18_BattlePass", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BR_Season18_BattlePass.DAv2_BR_Season18_BattlePass", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BR_BattlePass_Tiers25Levels.DAv2_BR_BattlePass_Tiers25Levels", ItemShopVisited),("v2:/9b91076467e61cf01a3c16e39a18331d2e23d754cdafc860aac0fdd7155615ae", ItemShopVisited),("v2:/83ac0269acedb2d5634a031f55b643b852272903e74d9fa1bb49256a0c06abef", ItemShopVisited),("v2:/aacc97a394a9feaa106ad275caad4e4f22b987d8ceb42d64991024bf6d8a5404", ItemShopVisited),("v2:/4f1c82dc8fb66fef5a0046fb2163344069b65b6ba64e496939d2fc8e8f779157", ItemShopVisited),("v2:/d9fe40e917bf98babee1c239153990efe3e1a568dd0e985c663dbba228eef03f", ItemShopVisited),("v2:/fd2b5edc1839496be18a0cb1ef1bc74c07f391b4448de53d07bb63f695f1763b", ItemShopVisited),("v2:/bfd337ddb7380a663929ae0ad03f6cdbff5b562d1639c8c813cb8316b37f83bb", ItemShopVisited),("v2:/d8c8f59ca26294a0192676567f75ee6c3631f96eea201fd14f8cac0c47acfb5c", ItemShopVisited),("v2:/cb671813542b9346ea26bfb3a53624fee2b73c4d2280c21b37c0bb0759c67574", ItemShopVisited),("v2:/9af32d7a9a16f864eae99d17542ec08763d118f3ce9c72ad05d5fc5f44586dc1", ItemShopVisited),("v2:/8ab132beb750c221f51a79c6b29d10abf9cf7e6a82868226d98abea8add01ac5", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Subs_CrewBling.DAv2_Subs_CrewBling", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_WinterQuest2019.DA_WinterQuest2019", ItemShopVisited),("B5FCB8D440CAB93A3080798FACEB77A3", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_Featured_CID_479_Athena_Commando_F_Davinci.DA_Featured_CID_479_Athena_Commando_F_Davinci", ItemShopVisited),("/Game/Items/CardPacks/Events/2021_Anniversary/CardPack_Event_2021_Anniversary.CardPack_Event_2021_Anniversary", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Bronze.CardPack_Bronze", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Jackpot.CardPack_Jackpot", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Basic.CardPack_Basic", ItemShopVisited),("/Game/Items/CardPacks/Events/Release/CardPack_Event_Persistent_Fortnitemares.CardPack_Event_Persistent_Fortnitemares", ItemShopVisited),("70DBDA11425B10AF7A005D82DB54BC59", ItemShopVisited),("A3C3EBCAE56E4B9C979806EF53EBD990", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season11_BattlePassWithLevels.DA_BR_Season11_BattlePassWithLevels", ItemShopVisited),("/Game/Items/CardPacks/SpecificRewards/CardPack_Custom_Firecracker_R.CardPack_Custom_Firecracker_R", ItemShopVisited),("v2:/a4261136772b6cf8ed774286a7e1b9a70c48748c066f5fd9f92d6f3ffec4fa2d", ItemShopVisited),("v2:/fd11007f66ba967aaa52ae91583956ed5832f9c69ef2a16f67a51995b37ff66e", ItemShopVisited),("v2:/0eaa77ea933a601a1355dfdd4295d43b7d7e0afef1913396992e2225beb7ab1b", ItemShopVisited),("v2:/9293a2edde97f7dde84803c9c38b3aa34c500edf5e6d3c85902b1458459ac047", ItemShopVisited),("v2:/9338a4d7b6f7ecd7fac8af6886b632930ff06585a53c61cc948f20988c89df61", ItemShopVisited),("v2:/a99955b726585b189886bc82e762cea29912fefeb454b417c06c037b18258153", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_914_F_York_E.DAv2_CID_914_F_York_E", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_264_F_HeadbandS.DAv2_CID_A_264_F_HeadbandS", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_704_HeadbandKMale1H.DAv2_Pickaxe_ID_704_HeadbandKMale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_LSID_367_Paperbag_3WGO8.DAv2_LSID_367_Paperbag_3WGO8", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_491_YorkMale.DAv2_Pickaxe_ID_491_YorkMale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_263_M_HeadbandS.DAv2_CID_A_263_M_HeadbandS", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_WindMillFloss.DAv2_EID_WindMillFloss", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_706_HeadbandStandAloneMale.DAv2_Pickaxe_ID_706_HeadbandStandAloneMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_752_M_Comet.DAv2_CID_752_M_Comet", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_913_F_York_D.DAv2_CID_913_F_York_D", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_York_AllM.DAv2_Bundles_York_AllM", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_Lars.DAv2_RMT_Lars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_262_M_HeadbandK.DAv2_CID_A_262_M_HeadbandK", OfferSectionVisited),("v2:/24cb005ee91e0a02b011b516c4cda2acfe0a10628166f5a2eb18d08b5a4144bc", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_703_HeadbandMale1H.DAv2_Pickaxe_ID_703_HeadbandMale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_634_YorkFemale.DAv2_BID_634_YorkFemale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_MusicPack_113_S18_FNCS.DAv2_MusicPack_113_S18_FNCS", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_079_F_Camo.DAv2_CID_079_F_Camo", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Chashu.DAv2_EID_Chashu", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_257_FrostMystery1H.DAv2_Pickaxe_ID_257_FrostMystery1H", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_912_F_York_C.DAv2_CID_912_F_York_C", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_635_YorkMale.DAv2_BID_635_YorkMale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_326_HeadbandMale.DAv2_Glider_ID_326_HeadbandMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_910_FNCS_Purple.DAv2_BID_910_FNCS_Purple", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_York_AllF.DAv2_Bundles_York_AllF", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_728_M_MinotaurLuck.DAv2_CID_728_M_MinotaurLuck", ItemShopVisited),("v2:/df986059874c41cd6166a832651e1ef4db73e680d923b773e603f4198b0fefd1", ItemShopVisited),("v2:/8c4bb56472a576556545c092fedf29361326650dfafb2b9127082dcdb2c1fd61", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_FrostMystery.DAv2_Bundle_Featured_FrostMystery", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_York_AllItems.DAv2_Bundles_York_AllItems", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_271_M_FNCS_Purple.DAv2_CID_A_271_M_FNCS_Purple", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_910_F_York_A.DAv2_CID_910_F_York_A", ItemShopVisited),("v2:/62b63ab848097523c5f9c26782fc5f5cdb9fccae5029d429d100b1ebeeb692da", ItemShopVisited),("v2:/307ad0988b2c104fc1a4e079fe02cc1b765defd2943fb5f00421aba4ee945b4f", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_DerbyDynamo.DAv2_RMT_DerbyDynamo", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_DarkReflections.DAv2_RMT_DarkReflections", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MintyLegends.DAv2_RMT_MintyLegends", OfferSectionVisited),("v2:/0e2442f8a596aff51eb51c7f6a9e4c6fb8788034efeeb769c7189fedf9fb43dc", ItemShopVisited),("v2:/6664177d3c1f7f0a24019f48ad2308b84c7bb2b348b6a9f4d6b93046a8970f97", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Headband_Bundle.DAv2_Bundle_Featured_Headband_Bundle", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_HeadbandGear_Bundle.DAv2_Bundle_Featured_HeadbandGear_Bundle", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_HeadbandB_Bundle.DAv2_Bundle_Featured_HeadbandB_Bundle", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_261_M_Headband.DAv2_CID_A_261_M_Headband", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Headband.DAv2_EID_Headband", OfferSectionVisited),("v2:/e7b0736943d5fb68d7ec927a082941c81deedba9bc78c6795278de67fa8a2da0", ItemShopVisited),("v2:/6a692f5ee7b517106c0fcb5735376ef0d9179b84399963ea3e3614eb70541d01", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Bronze_Melee.CardPack_Bronze_Melee", ItemShopVisited),("v2:/581d02fbbb52f9185f1acd58f0a400fda755d6532f234ee1141ab9b336185292", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Eerie_8WGYK.DAv2_EID_Eerie_8WGYK", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_817_CometSummer.DAv2_BID_817_CometSummer", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Mime.DAv2_EID_Mime", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_248_York.DAv2_Glider_ID_248_York", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_911_F_York_B.DAv2_CID_911_F_York_B", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_386_CometMale.DAv2_Pickaxe_ID_386_CometMale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_KpopDance01.DAv2_EID_KpopDance01", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_909_M_York_E.DAv2_CID_909_M_York_E", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_536_F_DurrBurgerWorker.DAv2_CID_536_F_DurrBurgerWorker", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_ClimbTheStaff.DAv2_EID_ClimbTheStaff", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_906_M_York_B.DAv2_CID_906_M_York_B", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_184_M_DurrBurgerWorker.DAv2_CID_184_M_DurrBurgerWorker", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_905_M_York_A.DAv2_CID_905_M_York_A", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_BurgerFlipping.DAv2_EID_BurgerFlipping", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_907_M_York_C.DAv2_CID_907_M_York_C", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_908_M_York_D.DAv2_CID_908_M_York_D", ItemShopVisited))\\nn'
                        'LastSelectedPlaylist=(PlaylistName="Playlist_DefaultDuo",TournamentId="",EventWindowId="",RegionId="BR",Mnemonic="playlist_defaultduo",MatchmakingRulePreset=RespectParties)\n'
                        "LastSelectedFillOption=True\n"
                        "bLastSelectedPrivateMatchOption=False\n"
                        "CustomMatchOptions=()\n"
                        "CreativeOptions=()\n"
                        "bHasSeenCreativePhoneTutorial=False\n"
                        "bHasSeenCreativeHeatmapTutorial=False\n"
                        "CreativeOptionLastUsedCategory=0\n"
                        "CreativeOptionLastUsedIndexInCategory=0\n"
                        "LastNewsVersionViewedBR=\n"
                        "LastNewsVersionViewedCreative=2021-09-22T22:44:27.601Z\n"
                        "LastNewsVersionViewedSTW=\n"
                        "LastPRMEtag=d28efcb1fba91bf9bfe4e2638ef34c00\n"
                        "LastFrontEndBackPlateStageUsed[0]=season18\n"
                        "LastFrontEndBackPlateStageUsed[1]=default\n"
                        "bEulaAccepted=True\n"
                        "EulaAcceptedUserId=972a2732bb54415896960a3a11d05194\n"
                        "LastEulaCheckTime=2021.11.19-17.02.42\n"
                        "HUDLayoutData[0]=(LayoutEntries=)\n"
                        "HUDLayoutData[1]=(LayoutEntries=)\n"
                        "HUDLayoutData[2]=(LayoutEntries=)\n"
                        "ActiveHUDProfileIdentifier=(HUDProfileType=(TagName=""),Guid=00000000000000000000000000000000)\n"
                        "bTimesSeenBacchusLoadTutorial=0\n"
                        "bHasSeenTapToShoot=False\n"
                        "NumTimesSeeingPanningTip=0\n"
                        "FireModeData=(bAutoFireIsEnabled=True,b3DTouchEnabled=False,bTapToShootEnabled=False,bAlwaysShowDedicatedButton=True,FireModeType=Unset)\n"
                        "SimpleMobileStats=(GamesPlayed=148,SecondsPlayed=76668,KillCount=478,BestResult=100,LastReviewPromptDay=0001.01.01-00.00.00,CampaignGamesPlayed=0)\n"
                        "AudioOutputDeviceId=\n"
                        "bUseHeadphoneMode=False\n"
                        "InitialBenchmarkState=1\n"
                        "bDisableMouseAcceleration=False\n"
                        "ChosenLoginType=None\n"
                        "SocialImportOptedOutVersion=1\n"
                        "VKImportOptedOutVersion=0\n"
                        "bHasSeenErebusSocialImport=False\n"
                        "bHasSeenFriendImportToast=False\n"
                        "LastSocialImportPromptTime=2021.09.24-13.02.09\n"
                        "bAutoImportFriendEnabled=False\n"
                        "bSeenLetoSellModal=False\n"
                        "SocialImportPromptCountCurrentVersion=1\n"
                        "SocialImportPromptCountAllVersions=1\n"
                        "VKImportPromptCountCurrentVersion=0\n"
                        "VKImportPromptCountAllVersions=0\n"
                        "LastAccountItemWarningTime=0001.01.01-00.00.00\n"
                        "bMultiFactorAuthModalOpOut=False\n"
                        "LastEnableMFAModalPromptTime=0001.01.01-00.00.00\n"
                        "LastVKImportPromptTime=0001.01.01-00.00.00\n"
                        "LastAffiliateToastTime=0001.01.01-00.00.00\n"
                        'FailedInviteMap=(("c902c685432c41fd9e7c1c9b05b607aa", 2021.11.19-14.20.38),("df148a35f9e64fa3bac3834ec2b9a8cb", 2021.11.19-14.14.11))\n'
                        "MobileRecommendationDismissedVersion=0\n"
                        "ShowLiveStreamPictureInPictureInMatchV2=Hide\n"
                        "CurrentLivePiPStreamOverrideCounter=0\n"
                        "SelectedFrontEnd=\n"
                        "bNeverShowMobileLink=False\n"
                        "bHasMigratedDownloadSettings=False\n"
                        "bSendAppsFlyerEventOnInstallation=True\n"
                        "bAllowFullGameDownload=False\n"
                        "bAllowCellularDownload=False\n"
                        "bAutoDownloadHighResTextures=False\n"
                        "LastAutoDownloadHighResTextureReminder=0\n"
                        "bAutoLaunchFullGame=False\n"
                        "bAllowDownloadHighResMips=True\n"
                        "bAllowLowPowerMode=False\n"
                        "bAllowVideoPlayback=True\n"
                        "bAllowMultithreadedRendering=True\n"
                        "MobileFPSMode=Mode_30Fps\n"
                        "MobileQualitySettingsResetDefaultsGUID=\n"
                        "bHasSeenSamsungPressureSensorWarning=False\n"
                        "bNeverDisplaySamsungPressureSensorWarning=False\n"
                        "bHasRecentlySeenBadMatchPopup=False\n"
                        "MatchesSinceLastBadMatchPopup=0\n"
                        "bHasAlreadyRatedOnGooglePlay=False\n"
                        "DaysToSnoozeBeforeNextGooglePlayRating=0\n"
                        "GooglePlayRatingDelayedOccurences=0\n"
                        "bShowTemperature=False\n"
                        "LastGameStartNotificationSentTime=0001.01.01-00.00.00\n"
                        "LastYearForcedDisplayWinterfestInfoButton=0\n"
                        "bHasSeenSidekickWelcomePopup=False\n"
                        "bPCMigratedToNextGenScalability=True\n"
                        "bUseVSync=False\n"
                        "bUseDynamicResolution=False\n"
                        "ResolutionSizeX=1024\n"
                        "ResolutionSizeY=768\n"
                        "LastUserConfirmedResolutionSizeX=1024\n"
                        "LastUserConfirmedResolutionSizeY=768\n"
                        "WindowPosX=-1\n"
                        "WindowPosY=-1\n"
                        "LastConfirmedFullscreenMode=1\n"
                        "PreferredFullscreenMode=0\n"
                        "AudioQualityLevel=0\n"
                        "LastConfirmedAudioQualityLevel=0\n"
                        "FrameRateLimit=240.000000\n"
                        "DesiredScreenWidth=1024\n"
                        "DesiredScreenHeight=768\n"
                        "LastUserConfirmedDesiredScreenWidth=1024\n"
                        "LastUserConfirmedDesiredScreenHeight=768\n"
                        "LastRecommendedScreenWidth=-1.000000\n"
                        "LastRecommendedScreenHeight=-1.000000\n"
                        "LastCPUBenchmarkResult=-1.000000\n"
                        "LastGPUBenchmarkResult=-1.000000\n"
                        "LastGPUBenchmarkMultiplier=1.000000\n"
                        "bUseHDRDisplayOutput=False\n"
                        "HDRDisplayOutputNits=1000\n"
                        "UserRenderingAPI=0\n"
                        "bGoalPagePinTooltipViewed=True\n"
                        'ItemShopSectionsSeenStateLastResetDates=(("Featured", 0001.01.01-00.00.00),("LimitedTime", 0001.01.01-00.00.00),("BattlePass", 0001.01.01-00.00.00),("Subscription", 0001.01.01-00.00.00),("Daily", 0001.01.01-00.00.00),("Special", 0001.01.01-00.00.00),("NarutoB", 0001.01.01-00.00.00),("GhostbustersGear", 0001.01.01-00.00.00),("Ghostbusters2", 0001.01.01-00.00.00),("Ghostbusters", 0001.01.01-00.00.00),("Naruto2B", 0001.01.01-00.00.00),("Naruto3B", 0001.01.01-00.00.00))\n'
                        "AutoDownloadHighResTexturesBehavior=Enabled\n"
                        "ContentQualityLevelSelected=Unset\n"
                        "FrontendFrameRateLimit=60\n"
                        "CurrentLockerSorts=((Character, Invalid))\n"
                        "\n" 
                        "[ScalabilityGroups]\n"
                        "sg.ResolutionQuality=100\n"
                        "sg.ViewDistanceQuality=1\n"
                        "sg.AntiAliasingQuality=0\n"
                        "sg.ShadowQuality=0\n"
                        "sg.PostProcessQuality=0\n"
                        "sg.TextureQuality=0\n"
                        "sg.EffectsQuality=0\n"
                        "sg.FoliageQuality=0\n"
                        "sg.ShadingQuality=0\n"
                        "\n"
                        "[ChatSettings]\n"
                        "HideSocialName=False\n"
                        "AutoImportFriends=False\n"
                        "AutoDeclineFriendRequests=False\n"
                        "ShowNotifications=True\n"
                        "NeverFadeMessages=True\n"
                        "ShowTimeStamps=True\n"
                        "ShowWhispersInAllTabs=True\n"
                        "ShowCustomTab=False\n"
                        "ShowWhispersTab=True\n"
                        "ShowGlobalTab=True\n"
                        "ShowCombatAndEventsTab=False\n"
                        "ShowClanTabs=False\n"
                        "HideOffline=False\n"
                        "HideOutgoing=False\n"
                        "HideSuggestions=False\n"
                        "HideRecent=False\n"
                        "HideBlocked=True\n"
                        "FilterMatureLanguage=True\n"
                        "DisplayCharacterNames=False\n"
                        "FriendInviteReceivedCueEnabled=False\n"
                        "GameOrPartyInviteReceivedCueEnabled=True\n"
                        "MessageReceivedCueEnabled=False\n"
                        "SoundEnabled=False\n"
                        "ShowTextChat=True\n"
                        "FontSize=1\n"
                        "WindowHeight=0\n"
                        "WindowOpacity=0.5\n"
                        "\n"
                        "[D3DRHIPreference]\n"
                        "bUseD3D12InGame=False\n"
                        "bPreferFeatureLevelES31=True\n"
                        "\n"
                        "[ShaderPipelineCache.CacheFile]\n"
                        "LastOpened=FortniteGame\n"
                        "\n"
                        "[PerformanceMode]\n"
                        "MeshQuality=0\n")
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi criada com sucesso !\n :)')
            elif varchk.get() == 1:
                with open(fr'C:\Users\{user}\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini', 'w+') as file:
                    file.write(
                        "[/Script/FortniteGame.FortGameUserSettings]\n"
                        "FullscreenMode=1\n"
                        "UnlockConsoleFPS=False\n"
                        "SubGameSelectCount_Athena=18\n"
                        "SubGameLastSelectedTime_Athena=2021.11.19-14.20.26\n"
                        "SubGameSelectCount_Campaign=0\n"
                        "SubGameLastSelectedTime_Campaign=0001.01.01-00.00.00\n"
                        "LastTimeSettingsSnapshotUploaded=2021.11.19-17.02.48\n"
                        "FirstLoginOnDevice=2021.09.23-10.47.07\n"
                        "SafeZone=1.000000\n"
                        "bIsSafeZoneSet=False\n"
                        "CachedPlayerLevel=59\n"
                        "bShowActorsWithSeasonItemTagMapIndicators=True\n"
                        "CachedBattleStars=0\n"
                        "CachedAlienStylePoints=0\n"
                        "CachedStylePoints=0\n"
                        'CachedClaimableRewards=(("Reward", 68),("Customization", 12))\n'
                        "CachedHighestBattlePassUnlockedPage=1\n"
                        "bShowCareerTabBang=True\n"
                        "FrontendQuestTooltipDisplayedCount=2\n"
                        "CustomVoiceChatInputDevice=\n"
                        "CustomVoiceChatOutputDevice=\n"
                        "CustomVoiceChatInputDeviceId=\n"
                        "CustomVoiceChatOutputDeviceId=\n"
                        "bMotionBlur=False\n"
                        "bShowGrass=False\n"
                        "bShowFPS=True\n"
                        "bUseGPUCrashDebugging=False\n"
                        "bLatencyTweak1=False\n"
                        "LatencyTweak2=1\n"
                        "bLatencyFlash=False\n"
                        "DLSSQuality=0\n"
                        "bRayTracing=False\n"
                        "RayTracingShadowsQuality=True\n"
                        "RayTracingReflectionsQuality=0\n"
                        "RayTracingAmbientOcclusionQuality=True\n"
                        "RayTracingAOQuality=0\n"
                        "RayTracingGIQuality=0\n"
                        "b120FpsMode=False\n"
                        "DisplayGamma=2.200000\n"
                        "UserInterfaceContrast=1.000000\n"
                        "NamedTimes=()\n"
                        'NamedCounts=(("lastfrontendflow_Fortnite", 18),("lastfrontendflow_Fortnite_HotfixVer", 0),("Cube_Queen_Cinematic", 18),("Cube_Queen_Cinematic_HotfixVer", 0),("FNmares_Ariana_Emote", 18),("FNmares_Ariana_Emote_HotfixVer", 0),("STARS_Team_intro", 18),("STARS_Team_intro_HotfixVer", 0),("November_Crew", 18),("November_Crew_HotfixVer", 0),("Jinx_Video", 18),("Jinx_Video_HotfixVer", 0),("DiscoveryLobbyMatchmakingPlay", 18),("DiscoveryLobbyMatchmakingPlay_HotfixVer", 0),("Naruto_Cinematic", 18),("Naruto_Cinematic_HotfixVer", 0),("BRUTE_War_Effort", 18),("BRUTE_War_Effort_HotfixVer", 0),("UEnableMultiFactorModal::ShouldShowMFASplashScreen", 18),("UEnableMultiFactorModal::ShouldShowMFASplashScreen_HotfixVer", 0),("FrontendContext:ShouldShowSocialImport", 18),("FrontendContext:ShouldShowSocialImport_HotfixVer", 0)\n)'
                        'BattlePassOverrideTracker=0\n'
                        'CrewBlingItemShopViolatorUnlockedStagesWhenDisplayed=0\n'
                        "bHasSeenCrewBlingTabBangs=False\n"
                        "bHasSeenDonutShopSequence=False\n"
                        "DonutIdleGameHighScore=0.000000\n"
                        'DisplayAssetPathToOfferSeenLevel=(("v2:/f9e24b8d4b7ab325a4487729d9cf969c750f859a95c7a690de20f79b8df82822", ItemShopVisited),("v2:/8f22f5b37116fd357b6192af46714995ff7d12ea6157980d2d075453c0426492", ItemShopVisited),("v2:/1023f2d8d0984911e2fe3a1fdf23b70a7218189b411bca81a0e493abd5b59677", ItemShopVisited),("v2:/83c2c7dd1240222394ed9c7415fbce183d8504842eebc30039ce96c929d365e6", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_AngelDarkStarterPack.DAv2_RMT_AngelDarkStarterPack", OfferSectionVisited),("v2:/22810a78f6e6f0ede3fdd932101b41347c895a519851438f40bc4f6aa4361bf0", ItemShopVisited),("v2:/3123175e86a2eb2e7e2c0142d72bbee17e21e5e02326d7b12e00280498ddb18a", ItemShopVisited),("v2:/e789e06787eca79f4102ef909578d7696798e148d0550c775e79a61ab4a35a2e", ItemShopVisited),("v2:/222374fc7ea9f6ef8eb0b3c20f3a5d7f64f612e9f3435c74e3d51d785739bf9f", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MagmaMasters.DAv2_RMT_MagmaMasters", OfferSectionVisited),("v2:/570ff3bed6fc8a1f7006610dbb6ce9e4bcd244a32caa435a60392460da356c88", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MaskedDancer.DAv2_RMT_MaskedDancer", ItemShopVisited),("v2:/6633ab8087f2a2e80bdf7a90d06351e7a03b82790cc2e286f4b6851020532ed4", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack1000.DA_MtxPack1000", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack2800.DA_MtxPack2800", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_Featured_LarsBundle.DA_Featured_LarsBundle", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack5000.DA_MtxPack5000", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_MtxPack13500.DA_MtxPack13500", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season11_BattlePass.DA_BR_Season11_BattlePass", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season18_BattlePass.DA_BR_Season18_BattlePass", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BR_Season18_BattlePass.DAv2_BR_Season18_BattlePass", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BR_BattlePass_Tiers25Levels.DAv2_BR_BattlePass_Tiers25Levels", ItemShopVisited),("v2:/9b91076467e61cf01a3c16e39a18331d2e23d754cdafc860aac0fdd7155615ae", ItemShopVisited),("v2:/83ac0269acedb2d5634a031f55b643b852272903e74d9fa1bb49256a0c06abef", ItemShopVisited),("v2:/aacc97a394a9feaa106ad275caad4e4f22b987d8ceb42d64991024bf6d8a5404", ItemShopVisited),("v2:/4f1c82dc8fb66fef5a0046fb2163344069b65b6ba64e496939d2fc8e8f779157", ItemShopVisited),("v2:/d9fe40e917bf98babee1c239153990efe3e1a568dd0e985c663dbba228eef03f", ItemShopVisited),("v2:/fd2b5edc1839496be18a0cb1ef1bc74c07f391b4448de53d07bb63f695f1763b", ItemShopVisited),("v2:/bfd337ddb7380a663929ae0ad03f6cdbff5b562d1639c8c813cb8316b37f83bb", ItemShopVisited),("v2:/d8c8f59ca26294a0192676567f75ee6c3631f96eea201fd14f8cac0c47acfb5c", ItemShopVisited),("v2:/cb671813542b9346ea26bfb3a53624fee2b73c4d2280c21b37c0bb0759c67574", ItemShopVisited),("v2:/9af32d7a9a16f864eae99d17542ec08763d118f3ce9c72ad05d5fc5f44586dc1", ItemShopVisited),("v2:/8ab132beb750c221f51a79c6b29d10abf9cf7e6a82868226d98abea8add01ac5", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Subs_CrewBling.DAv2_Subs_CrewBling", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_WinterQuest2019.DA_WinterQuest2019", ItemShopVisited),("B5FCB8D440CAB93A3080798FACEB77A3", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_Featured_CID_479_Athena_Commando_F_Davinci.DA_Featured_CID_479_Athena_Commando_F_Davinci", ItemShopVisited),("/Game/Items/CardPacks/Events/2021_Anniversary/CardPack_Event_2021_Anniversary.CardPack_Event_2021_Anniversary", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Bronze.CardPack_Bronze", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Jackpot.CardPack_Jackpot", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Basic.CardPack_Basic", ItemShopVisited),("/Game/Items/CardPacks/Events/Release/CardPack_Event_Persistent_Fortnitemares.CardPack_Event_Persistent_Fortnitemares", ItemShopVisited),("70DBDA11425B10AF7A005D82DB54BC59", ItemShopVisited),("A3C3EBCAE56E4B9C979806EF53EBD990", ItemShopVisited),("/Game/Catalog/DisplayAssets/DA_BR_Season11_BattlePassWithLevels.DA_BR_Season11_BattlePassWithLevels", ItemShopVisited),("/Game/Items/CardPacks/SpecificRewards/CardPack_Custom_Firecracker_R.CardPack_Custom_Firecracker_R", ItemShopVisited),("v2:/a4261136772b6cf8ed774286a7e1b9a70c48748c066f5fd9f92d6f3ffec4fa2d", ItemShopVisited),("v2:/fd11007f66ba967aaa52ae91583956ed5832f9c69ef2a16f67a51995b37ff66e", ItemShopVisited),("v2:/0eaa77ea933a601a1355dfdd4295d43b7d7e0afef1913396992e2225beb7ab1b", ItemShopVisited),("v2:/9293a2edde97f7dde84803c9c38b3aa34c500edf5e6d3c85902b1458459ac047", ItemShopVisited),("v2:/9338a4d7b6f7ecd7fac8af6886b632930ff06585a53c61cc948f20988c89df61", ItemShopVisited),("v2:/a99955b726585b189886bc82e762cea29912fefeb454b417c06c037b18258153", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_914_F_York_E.DAv2_CID_914_F_York_E", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_264_F_HeadbandS.DAv2_CID_A_264_F_HeadbandS", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_704_HeadbandKMale1H.DAv2_Pickaxe_ID_704_HeadbandKMale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_LSID_367_Paperbag_3WGO8.DAv2_LSID_367_Paperbag_3WGO8", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_491_YorkMale.DAv2_Pickaxe_ID_491_YorkMale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_263_M_HeadbandS.DAv2_CID_A_263_M_HeadbandS", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_WindMillFloss.DAv2_EID_WindMillFloss", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_706_HeadbandStandAloneMale.DAv2_Pickaxe_ID_706_HeadbandStandAloneMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_752_M_Comet.DAv2_CID_752_M_Comet", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_913_F_York_D.DAv2_CID_913_F_York_D", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_York_AllM.DAv2_Bundles_York_AllM", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_Lars.DAv2_RMT_Lars", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_262_M_HeadbandK.DAv2_CID_A_262_M_HeadbandK", OfferSectionVisited),("v2:/24cb005ee91e0a02b011b516c4cda2acfe0a10628166f5a2eb18d08b5a4144bc", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_703_HeadbandMale1H.DAv2_Pickaxe_ID_703_HeadbandMale1H", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_634_YorkFemale.DAv2_BID_634_YorkFemale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_MusicPack_113_S18_FNCS.DAv2_MusicPack_113_S18_FNCS", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_079_F_Camo.DAv2_CID_079_F_Camo", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Chashu.DAv2_EID_Chashu", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_257_FrostMystery1H.DAv2_Pickaxe_ID_257_FrostMystery1H", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_912_F_York_C.DAv2_CID_912_F_York_C", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_635_YorkMale.DAv2_BID_635_YorkMale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_326_HeadbandMale.DAv2_Glider_ID_326_HeadbandMale", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_910_FNCS_Purple.DAv2_BID_910_FNCS_Purple", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_York_AllF.DAv2_Bundles_York_AllF", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_728_M_MinotaurLuck.DAv2_CID_728_M_MinotaurLuck", ItemShopVisited),("v2:/df986059874c41cd6166a832651e1ef4db73e680d923b773e603f4198b0fefd1", ItemShopVisited),("v2:/8c4bb56472a576556545c092fedf29361326650dfafb2b9127082dcdb2c1fd61", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_FrostMystery.DAv2_Bundle_Featured_FrostMystery", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundles_York_AllItems.DAv2_Bundles_York_AllItems", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_271_M_FNCS_Purple.DAv2_CID_A_271_M_FNCS_Purple", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_910_F_York_A.DAv2_CID_910_F_York_A", ItemShopVisited),("v2:/62b63ab848097523c5f9c26782fc5f5cdb9fccae5029d429d100b1ebeeb692da", ItemShopVisited),("v2:/307ad0988b2c104fc1a4e079fe02cc1b765defd2943fb5f00421aba4ee945b4f", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_DerbyDynamo.DAv2_RMT_DerbyDynamo", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_DarkReflections.DAv2_RMT_DarkReflections", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_RMT_MintyLegends.DAv2_RMT_MintyLegends", OfferSectionVisited),("v2:/0e2442f8a596aff51eb51c7f6a9e4c6fb8788034efeeb769c7189fedf9fb43dc", ItemShopVisited),("v2:/6664177d3c1f7f0a24019f48ad2308b84c7bb2b348b6a9f4d6b93046a8970f97", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_Headband_Bundle.DAv2_Bundle_Featured_Headband_Bundle", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_HeadbandGear_Bundle.DAv2_Bundle_Featured_HeadbandGear_Bundle", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Bundle_Featured_HeadbandB_Bundle.DAv2_Bundle_Featured_HeadbandB_Bundle", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_A_261_M_Headband.DAv2_CID_A_261_M_Headband", OfferSectionVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Headband.DAv2_EID_Headband", OfferSectionVisited),("v2:/e7b0736943d5fb68d7ec927a082941c81deedba9bc78c6795278de67fa8a2da0", ItemShopVisited),("v2:/6a692f5ee7b517106c0fcb5735376ef0d9179b84399963ea3e3614eb70541d01", ItemShopVisited),("/Game/Items/CardPacks/CardPack_Bronze_Melee.CardPack_Bronze_Melee", ItemShopVisited),("v2:/581d02fbbb52f9185f1acd58f0a400fda755d6532f234ee1141ab9b336185292", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Eerie_8WGYK.DAv2_EID_Eerie_8WGYK", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_BID_817_CometSummer.DAv2_BID_817_CometSummer", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_Mime.DAv2_EID_Mime", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Glider_ID_248_York.DAv2_Glider_ID_248_York", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_911_F_York_B.DAv2_CID_911_F_York_B", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_Pickaxe_ID_386_CometMale.DAv2_Pickaxe_ID_386_CometMale", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_KpopDance01.DAv2_EID_KpopDance01", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_909_M_York_E.DAv2_CID_909_M_York_E", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_536_F_DurrBurgerWorker.DAv2_CID_536_F_DurrBurgerWorker", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_ClimbTheStaff.DAv2_EID_ClimbTheStaff", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_906_M_York_B.DAv2_CID_906_M_York_B", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_184_M_DurrBurgerWorker.DAv2_CID_184_M_DurrBurgerWorker", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_905_M_York_A.DAv2_CID_905_M_York_A", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_EID_BurgerFlipping.DAv2_EID_BurgerFlipping", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_907_M_York_C.DAv2_CID_907_M_York_C", ItemShopVisited),("/Game/Catalog/NewDisplayAssets/DAv2_CID_908_M_York_D.DAv2_CID_908_M_York_D", ItemShopVisited))\\nn'
                        'LastSelectedPlaylist=(PlaylistName="Playlist_DefaultDuo",TournamentId="",EventWindowId="",RegionId="BR",Mnemonic="playlist_defaultduo",MatchmakingRulePreset=RespectParties)\n'
                        "LastSelectedFillOption=True\n"
                        "bLastSelectedPrivateMatchOption=False\n"
                        "CustomMatchOptions=()\n"
                        "CreativeOptions=()\n"
                        "bHasSeenCreativePhoneTutorial=False\n"
                        "bHasSeenCreativeHeatmapTutorial=False\n"
                        "CreativeOptionLastUsedCategory=0\n"
                        "CreativeOptionLastUsedIndexInCategory=0\n"
                        "LastNewsVersionViewedBR=\n"
                        "LastNewsVersionViewedCreative=2021-09-22T22:44:27.601Z\n"
                        "LastNewsVersionViewedSTW=\n"
                        "LastPRMEtag=d28efcb1fba91bf9bfe4e2638ef34c00\n"
                        "LastFrontEndBackPlateStageUsed[0]=season18\n"
                        "LastFrontEndBackPlateStageUsed[1]=default\n"
                        "bEulaAccepted=True\n"
                        "EulaAcceptedUserId=972a2732bb54415896960a3a11d05194\n"
                        "LastEulaCheckTime=2021.11.19-17.02.42\n"
                        "HUDLayoutData[0]=(LayoutEntries=)\n"
                        "HUDLayoutData[1]=(LayoutEntries=)\n"
                        "HUDLayoutData[2]=(LayoutEntries=)\n"
                        "ActiveHUDProfileIdentifier=(HUDProfileType=(TagName=""),Guid=00000000000000000000000000000000)\n"
                        "bTimesSeenBacchusLoadTutorial=0\n"
                        "bHasSeenTapToShoot=False\n"
                        "NumTimesSeeingPanningTip=0\n"
                        "FireModeData=(bAutoFireIsEnabled=True,b3DTouchEnabled=False,bTapToShootEnabled=False,bAlwaysShowDedicatedButton=True,FireModeType=Unset)\n"
                        "SimpleMobileStats=(GamesPlayed=148,SecondsPlayed=76668,KillCount=478,BestResult=100,LastReviewPromptDay=0001.01.01-00.00.00,CampaignGamesPlayed=0)\n"
                        "AudioOutputDeviceId=\n"
                        "bUseHeadphoneMode=False\n"
                        "InitialBenchmarkState=1\n"
                        "bDisableMouseAcceleration=False\n"
                        "ChosenLoginType=None\n"
                        "SocialImportOptedOutVersion=1\n"
                        "VKImportOptedOutVersion=0\n"
                        "bHasSeenErebusSocialImport=False\n"
                        "bHasSeenFriendImportToast=False\n"
                        "LastSocialImportPromptTime=2021.09.24-13.02.09\n"
                        "bAutoImportFriendEnabled=False\n"
                        "bSeenLetoSellModal=False\n"
                        "SocialImportPromptCountCurrentVersion=1\n"
                        "SocialImportPromptCountAllVersions=1\n"
                        "VKImportPromptCountCurrentVersion=0\n"
                        "VKImportPromptCountAllVersions=0\n"
                        "LastAccountItemWarningTime=0001.01.01-00.00.00\n"
                        "bMultiFactorAuthModalOpOut=False\n"
                        "LastEnableMFAModalPromptTime=0001.01.01-00.00.00\n"
                        "LastVKImportPromptTime=0001.01.01-00.00.00\n"
                        "LastAffiliateToastTime=0001.01.01-00.00.00\n"
                        'FailedInviteMap=(("c902c685432c41fd9e7c1c9b05b607aa", 2021.11.19-14.20.38),("df148a35f9e64fa3bac3834ec2b9a8cb", 2021.11.19-14.14.11))\n'
                        "MobileRecommendationDismissedVersion=0\n"
                        "ShowLiveStreamPictureInPictureInMatchV2=Hide\n"
                        "CurrentLivePiPStreamOverrideCounter=0\n"
                        "SelectedFrontEnd=\n"
                        "bNeverShowMobileLink=False\n"
                        "bHasMigratedDownloadSettings=False\n"
                        "bSendAppsFlyerEventOnInstallation=True\n"
                        "bAllowFullGameDownload=False\n"
                        "bAllowCellularDownload=False\n"
                        "bAutoDownloadHighResTextures=False\n"
                        "LastAutoDownloadHighResTextureReminder=0\n"
                        "bAutoLaunchFullGame=False\n"
                        "bAllowDownloadHighResMips=True\n"
                        "bAllowLowPowerMode=False\n"
                        "bAllowVideoPlayback=True\n"
                        "bAllowMultithreadedRendering=True\n"
                        "MobileFPSMode=Mode_30Fps\n"
                        "MobileQualitySettingsResetDefaultsGUID=\n"
                        "bHasSeenSamsungPressureSensorWarning=False\n"
                        "bNeverDisplaySamsungPressureSensorWarning=False\n"
                        "bHasRecentlySeenBadMatchPopup=False\n"
                        "MatchesSinceLastBadMatchPopup=0\n"
                        "bHasAlreadyRatedOnGooglePlay=False\n"
                        "DaysToSnoozeBeforeNextGooglePlayRating=0\n"
                        "GooglePlayRatingDelayedOccurences=0\n"
                        "bShowTemperature=False\n"
                        "LastGameStartNotificationSentTime=0001.01.01-00.00.00\n"
                        "LastYearForcedDisplayWinterfestInfoButton=0\n"
                        "bHasSeenSidekickWelcomePopup=False\n"
                        "bPCMigratedToNextGenScalability=True\n"
                        "bUseVSync=False\n"
                        "bUseDynamicResolution=False\n"
                        "ResolutionSizeX=1750\n"
                        "ResolutionSizeY=1080\n"
                        "LastUserConfirmedResolutionSizeX=1750\n"
                        "LastUserConfirmedResolutionSizeY=1080\n"
                        "WindowPosX=-1\n"
                        "WindowPosY=-1\n"
                        "LastConfirmedFullscreenMode=1\n"
                        "PreferredFullscreenMode=0\n"
                        "AudioQualityLevel=0\n"
                        "LastConfirmedAudioQualityLevel=0\n"
                        "FrameRateLimit=240.000000\n"
                        "DesiredScreenWidth=1750\n"
                        "DesiredScreenHeight=1080\n"
                        "LastUserConfirmedDesiredScreenWidth=1750\n"
                        "LastUserConfirmedDesiredScreenHeight=1080\n"
                        "LastRecommendedScreenWidth=-1.000000\n"
                        "LastRecommendedScreenHeight=-1.000000\n"
                        "LastCPUBenchmarkResult=-1.000000\n"
                        "LastGPUBenchmarkResult=-1.000000\n"
                        "LastGPUBenchmarkMultiplier=1.000000\n"
                        "bUseHDRDisplayOutput=False\n"
                        "HDRDisplayOutputNits=1000\n"
                        "UserRenderingAPI=0\n"
                        "bGoalPagePinTooltipViewed=True\n"
                        'ItemShopSectionsSeenStateLastResetDates=(("Featured", 0001.01.01-00.00.00),("LimitedTime", 0001.01.01-00.00.00),("BattlePass", 0001.01.01-00.00.00),("Subscription", 0001.01.01-00.00.00),("Daily", 0001.01.01-00.00.00),("Special", 0001.01.01-00.00.00),("NarutoB", 0001.01.01-00.00.00),("GhostbustersGear", 0001.01.01-00.00.00),("Ghostbusters2", 0001.01.01-00.00.00),("Ghostbusters", 0001.01.01-00.00.00),("Naruto2B", 0001.01.01-00.00.00),("Naruto3B", 0001.01.01-00.00.00))\n'
                        "AutoDownloadHighResTexturesBehavior=Enabled\n"
                        "ContentQualityLevelSelected=Unset\n"
                        "FrontendFrameRateLimit=240\n"
                        "CurrentLockerSorts=((Character, Invalid))\n"
                        "\n" 
                        "[ScalabilityGroups]\n"
                        "sg.ResolutionQuality=100\n"
                        "sg.ViewDistanceQuality=1\n"
                        "sg.AntiAliasingQuality=0\n"
                        "sg.ShadowQuality=0\n"
                        "sg.PostProcessQuality=0\n"
                        "sg.TextureQuality=0\n"
                        "sg.EffectsQuality=0\n"
                        "sg.FoliageQuality=0\n"
                        "sg.ShadingQuality=0\n"
                        "\n"
                        "[ChatSettings]\n"
                        "HideSocialName=False\n"
                        "AutoImportFriends=False\n"
                        "AutoDeclineFriendRequests=False\n"
                        "ShowNotifications=True\n"
                        "NeverFadeMessages=True\n"
                        "ShowTimeStamps=True\n"
                        "ShowWhispersInAllTabs=True\n"
                        "ShowCustomTab=False\n"
                        "ShowWhispersTab=True\n"
                        "ShowGlobalTab=True\n"
                        "ShowCombatAndEventsTab=False\n"
                        "ShowClanTabs=False\n"
                        "HideOffline=False\n"
                        "HideOutgoing=False\n"
                        "HideSuggestions=False\n"
                        "HideRecent=False\n"
                        "HideBlocked=True\n"
                        "FilterMatureLanguage=True\n"
                        "DisplayCharacterNames=False\n"
                        "FriendInviteReceivedCueEnabled=False\n"
                        "GameOrPartyInviteReceivedCueEnabled=True\n"
                        "MessageReceivedCueEnabled=False\n"
                        "SoundEnabled=False\n"
                        "ShowTextChat=True\n"
                        "FontSize=1\n"
                        "WindowHeight=0\n"
                        "WindowOpacity=0.5\n"
                        "\n"
                        "[D3DRHIPreference]\n"
                        "bUseD3D12InGame=False\n"
                        "bPreferFeatureLevelES31=True\n"
                        "\n"
                        "[ShaderPipelineCache.CacheFile]\n"
                        "LastOpened=FortniteGame\n"
                        "\n"
                        "[PerformanceMode]\n"
                        "MeshQuality=0\n")
                tk.messagebox.showinfo('Operação Concluída', 'Sua GameUserSettings foi substituída com sucesso !\n :)')
        except:
            tk.messagebox.showerror('Erro', 'Não foi possível modificar sua configuração, o jogo ou a configuração não foi encontrado(a) no sistema !\n :(')
    
    def btnGTAVAction():
        try:
            if varchk.get() == 2:
                tk.messagebox.showinfo('Importante', 'Selecione o diretório onde seu gta v está instalado (pasta raiz)!\n :)')
                directory = str(dlg.askdirectory(title='Selecione a configuração'))
                with open(fr'{directory}\Commandline.txt', 'w+') as file:
                    file.write(
                        "-norestrictions\n"
                        "-percentvidmem\n"
                        "-availablevidmem\n"
                        "-novblank\n"
                        "-nomemrestrict\n"
                        "-novblank\n"
                        "-noprecache\n"
                        "-framelimit 0\n"
                        "-dx10\n"
                        "-width 600\n"
                        "-height 800\n"
                        "-fullscreen\n"
                        "-ignoreDifferentVideoCard\n"
                        "-anisotropicQualityLeve (0)\n"
                        "-disableHyperthreading\n"
                        "-hdr\n"
                        "-useMinimumSettings\n"
                        "-HDStreamingInFlight\n"
                        "-pedLodBias\n"
                        "-grassQuality (0)\n"
                        "-noInGameDOF\n"
                        "-particleQuality (0)\n"
                        "-postFX (0)\n"
                        "-reflectionQuality (0)\n"
                        "-SSAO (0)\n"
                        "-shaderQuality (0)\n"
                        "-textureQuality (0)\n"
                        "-tessellation (0)\n"
                        "-fxaa (0)\n"
                        "-shadowQuality (0)\n"
                        )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi criada com sucesso !\n :)')
            elif varchk.get() == 3:
                tk.messagebox.showinfo('Importante', 'Selecione o diretório onde seu gta v está instalado (pasta raiz)!\n :)')
                directory = str(dlg.askdirectory(title='Selecione a configuração'))
                with open(fr'{directory}\Commandline.txt', 'w+') as file:
                    file.write(
                        "-norestrictions\n"
                        "-percentvidmem\n"
                        "-availablevidmem\n"
                        "-novblank\n"
                        "-nomemrestrict\n"
                        "-novblank\n"
                        "-noprecache\n"
                        "-framelimit 0\n"
                        "-dx11\n"
                        "-width 1920\n"
                        "-height 1080\n"
                        "-fullscreen\n"
                        "-ignoreDifferentVideoCard\n"
                        "-anisotropicQualityLeve (0)\n"
                        "-disableHyperthreading\n"
                        "-hdr\n"
                        "-HDStreamingInFlight\n"
                        "-pedLodBias\n"
                        "-grassQuality (0)\n"
                        "-noInGameDOF\n"
                        "-particleQuality (0)\n"
                        "-postFX (0)\n"
                        "-reflectionQuality (1)\n"
                        "-SSAO (0)\n"
                        "-shaderQuality (0)\n"
                        "-waterQuality (1)\n"
                        "-textureQuality (0)\n"
                        "-tessellation (0)\n"
                        "-fxaa (0)\n"
                        "-shadowQuality (0)\n"
                        )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi substituída com sucesso !\n :)')
        except: 
            tk.messagebox.showerror('Erro', 'Não foi possível modificar sua configuração, o jogo ou a configuração não foi encontrado(a) no sistema !\n :(')

    def btnWarzoneAction():
        try:
            if varchk.get() == 4:
                if os.path.isdir(f"C:/Users/{user}/Documents/Call of Duty Modern Warfare/players"):
                    tk.messagebox.showinfo('Importante', 'Não abra o jogo em modo de segurança nem dê permissão para o jogo modificar suas configurações gráficas !\n :)')
                    with open(fr'C:\Users\{user}\Documents\Call of Duty Modern Warfare\players\config.cfg', 'w+') as file:
                        file.write(
                            '// generated by KOCKIE to modify kkk\n'
                            'setcl 30049418 "140"\n'
                            'setcl 49997308 "0.5"\n'
                            'setcl 58932476 "S24D332"\n'
                            'setcl 75087430 "1"\n'
                            'setcl 100298170 "200"\n'
                            'setcl 135805301 "0.6"\n'
                            'setcl 174982485 "1.5"\n'
                            'setcl 194177937 "1"\n'
                            'setcl 204768854 "0"\n'
                            'setcl 218404237 "1"\n'
                            'setcl 228392943 "1.5"\n'
                            'setcl 239490324 "1"\n'
                            'setcl 263809092 "0"\n'
                            'setcl 281093946 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 283349319 "12"\n'
                            'setcl 300071733 "0"\n'
                            'setcl 300689787 "0.4749"\n'
                            'setcl 307701044 "0"\n'
                            'setcl 344232750 "1"\n'
                            'setcl 366728169 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 386839215 "0"\n'
                            'setcl 390858914 "0"\n'
                            'setcl 405012731 "1"\n'
                            'setcl 412725085 "1100"\n'
                            'setcl 431324756 "0"\n'
                            'setcl 438033235 "0.75"\n'
                            'setcl 442075206 "0.25"\n'
                            'setcl 452058051 "0"\n'
                            'setcl 459540817 "-1"\n'
                            'setcl 461165839 "1"\n'
                            'setcl 471390880 "0"\n'
                            'setcl 497895430 "-1"\n'
                            'setcl 500533217 "0"\n'
                            'setcl 502072820 "1"\n'
                            'setcl 503885063 "16.11.2"\n'
                            'setcl 506914818 "28"\n'
                            'setcl 524633178 "7"\n'
                            'setcl 530869264 "0.8"\n'
                            'setcl 549656596 "2072.43"\n'
                            'setcl 576994415 "0"\n'
                            'setcl 578190563 "MENU/DEFAULT_COMMUNICATION_DEVICE"\n'
                            'setcl 620032665 "1"\n'
                            'setcl 625258013 "subtitle"\n'
                            'setcl 631512172 "0"\n'
                            'setcl 649200945 "0"\n'
                            'setcl 651190804 "1.5"\n'
                            'setcl 656607832 "0"\n'
                            'setcl 662286220 "1"\n'
                            'setcl 670213830 "1.5"\n'
                            'setcl 683401118 "0"\n'
                            'setcl 695904642 "5"\n'
                            'setcl 728921641 "1"\n'
                            'setcl 741529514 "0"\n'
                            'setcl 763756775 "0.2625"\n'
                            'setcl 834974127 "None"\n'
                            'setcl 870012236 "420"\n'
                            'setcl 875970007 "1"\n'
                            'setcl 876099564 "2"\n'
                            'setcl 880871712 "0"\n'
                            'setcl 895653276 "800x600"\n'
                            'setcl 901605185 "0"\n'
                            'setcl 918242844 "3"\n'
                            'setcl 924246637 "1"\n'
                            'setcl 927356470 "Enabled"\n'
                            'setcl 971698222 "50"\n'
                            'setcl 993324516 "1"\n'
                            'setcl 1010551079 "30"\n'
                            'setcl 1023710916 "mw_default"\n'
                            'setcl 1089030849 "0"\n'
                            'setcl 1112114094 "1000"\n'
                            'setcl 1116474394 "1"\n'
                            'setcl 1120557623 "0.4"\n'
                            'setcl 1178686240 "330"\n'
                            'setcl 1267618646 "1"\n'
                            'setcl 1310823371 "0"\n'
                            'setcl 1389640589 "Off"\n'
                            'setcl 1392059387 "1"\n'
                            'setcl 1414304430 "375.70"\n'
                            'setcl 1429023948 "0.25"\n'
                            'setcl 1445079425 "0.8 0 0 1"\n'
                            'setcl 1455453918 "0"\n'
                            'setcl 1481207725 "1"\n'
                            'setcl 1503870259 "1"\n'
                            'setcl 1503912771 "1"\n'
                            'setcl 1511138344 "400"\n'
                            'setcl 1529983144 "0"\n'
                            'setcl 1539706852 "1"\n'
                            'setcl 1551683251 "1"\n'
                            'setcl 1589004716 "1"\n'
                            'setcl 1595752881 "1"\n'
                            'setcl 1607162157 "Off"\n'
                            'setcl 1612582153 "500"\n'
                            'setcl 1621853845 "-1"\n'
                            'setcl 1635259448 "0.25"\n'
                            'setcl 1649833455 "1"\n'
                            'setcl 1650431234 "75.000"\n'
                            'setcl 1659218611 "3"\n'
                            'setcl 1709018887 "BT709_sRGB"\n'
                            'setcl 1730559565 "-1"\n'
                            'setcl 1741328560 "1"\n'
                            'setcl 1756517702 "2"\n'
                            'setcl 1762842223 "0.5"\n'
                            'setcl 1766991848 "16 11 2"\n'
                            'setcl 1844320632 "1105920"\n'
                            'setcl 1847523626 "Enabled"\n'
                            'setcl 1870423823 "0.25"\n'
                            'setcl 1872772153 "1"\n'
                            'setcl 1878342628 "1"\n'
                            'setcl 1897730391 "0"\n'
                            'setcl 1906772039 "0"\n'
                            'setcl 1912904919 "0 0.6 0.18 1"\n'
                            'setcl 1947817761 "0.55"\n'
                            'setcl 1950622058 "100"\n'
                            'setcl 1959281112 "1.33"\n'
                            'setcl 2037202737 ""\n'
                            'setcl 2058006225 "65536"\n'
                            'setcl 2086828738 "8"\n'
                            'setcl 2107748520 "0.007"\n'
                            'setcl 2122379707 "0"\n'
                            'setcl 2135348401 "0.75"\n'
                            'setcl 2137916686 "0"\n'
                            'setcl 2142502956 "5"\n'
                            'setcl 2144662347 "0.5058"\n'
                            'setcl -2143051707 "1"\n'
                            'setcl -2139668929 "0"\n'
                            'setcl -2137405194 "0"\n'
                            'setcl -2117467049 "1"\n'
                            'setcl -2114644220 "1"\n'
                            'setcl -2105641424 "0"\n'
                            'setcl -2086531702 "0"\n'
                            'setcl -2085697508 "0.25"\n'
                            'setcl -2080133768 "1"\n'
                            'setcl -2074405569 "None"\n'
                            'setcl -2067023712 "1"\n'
                            'setcl -2056187699 "2"\n'
                            'setcl -2034804594 "720"\n'
                            'setcl -2023656898 "0.022"\n'
                            'setcl -2010075995 "TEXTURE_FILTER_NEAREST"\n'
                            'setcl -2002816811 "6"\n'
                            'setcl -1991645855 "5"\n'
                            'setcl -1981625429 "0"\n'
                            'setcl -1972948778 "0.03125 0.01"\n'
                            'setcl -1956509584 "1"\n'
                            'setcl -1955814596 "4.44051"\n'
                            'setcl -1946338041 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl -1915975709 "1"\n'
                            'setcl -1905118811 "5"\n'
                            'setcl -1893739580 "0"\n'
                            'setcl -1891132266 "1"\n'
                            'setcl -1867156735 "1"\n'
                            'setcl -1865705906 "0"\n'
                            'setcl -1842923869 "0.002"\n'
                            'setcl -1835563320 "1"\n'
                            'setcl -1814433719 "0"\n'
                            'setcl -1798389992 "0.25"\n'
                            'setcl -1788235984 "1"\n'
                            'setcl -1781237900 "10 0.1"\n'
                            'setcl -1733029737 "-1"\n'
                            'setcl -1726953279 "10"\n'
                            'setcl -1712782598 "76"\n'
                            'setcl -1700655082 "10"\n'
                            'setcl -1698080106 "1800"\n'
                            'setcl -1684289521 "7.94328"\n'
                            'setcl -1680234015 "1"\n'
                            'setcl -1663250207 "1"\n'
                            'setcl -1650980398 "1.99526"\n'
                            'setcl -1644964340 "1"\n'
                            'setcl -1641719278 "1"\n'
                            'setcl -1635690325 "4"\n'
                            'setcl -1628594889 "1"\n'
                            'setcl -1627085165 "0"\n'
                            'setcl -1588581417 "5"\n'
                            'setcl -1580595131 "0"\n'
                            'setcl -1580591086 "37570"\n'
                            'setcl -1578846674 "2000"\n'
                            'setcl -1557306549 "1"\n'
                            'setcl -1556678412 "-32768"\n'
                            'setcl -1548462097 "0"\n'
                            'setcl -1540799782 "0.4633"\n'
                            'setcl -1534246785 "Off"\n'
                            'setcl -1533549817 "50"\n'
                            'setcl -1500059242 "2"\n'
                            'setcl -1499628353 "120"\n'
                            'setcl -1495716865 "0.4981"\n'
                            'setcl -1492172900 "Fullscreen"\n'
                            'setcl -1485943526 "250"\n'
                            'setcl -1457215672 "Low"\n'
                            'setcl -1440857325 "gamenotify obituary"\n'
                            'setcl -1407078038 "1"\n'
                            'setcl -1403009210 "0.021961 1"\n'
                            'setcl -1340369237 "5"\n'
                            'setcl -1318801789 "0"\n'
                            'setcl -1315502002 "0.00 0.00"\n'
                            'setcl -1308994087 "15"\n'
                            'setcl -1275067384 "-32768"\n'
                            'setcl -1260932940 "1"\n'
                            'setcl -1256506668 ""\n'
                            'setcl -1253873949 "1"\n'
                            'setcl -1243427350 "boldgame"\n'
                            'setcl -1224461919 "1"\n'
                            'setcl -1223963406 "1"\n'
                            'setcl -1202901244 "100"\n'
                            'setcl -1163575897 "mw_default"\n'
                            'setcl -1110058394 "0.8 0.62"\n'
                            'setcl -1096719032 "64"\n'
                            'setcl -1014472453 "1"\n'
                            'setcl -1006049675 "0.25"\n'
                            'setcl -995223359 "0.25"\n'
                            'setcl -992918301 "16.6667"\n'
                            'setcl -967502985 "1"\n'
                            'setcl -951569131 "0"\n'
                            'setcl -918239492 "1"\n'
                            'setcl -903403054 "1"\n'
                            'setcl -871715026 "1"\n'
                            'setcl -869033783 "2"\n'
                            'setcl -860800213 "1"\n'
                            'setcl -826651178 "0.5"\n'
                            'setcl -820249539 "0.8"\n'
                            'setcl -820180432 "2"\n'
                            'setcl -813493907 "0 0.3 0.8 1"\n'
                            'setcl -803409955 "0.25"\n'
                            'setcl -795376234 "1"\n'
                            'setcl -757157143 "1"\n'
                            'setcl -727827321 "0.65"\n'
                            'setcl -726702765 "8129"\n'
                            'setcl -687558011 "1.9"\n'
                            'setcl -653426476 "0_Off"\n'
                            'setcl -652465405 "1"\n'
                            'setcl -641481682 "60"\n'
                            'setcl -623745089 "1"\n'
                            'setcl -616091757 "100"\n'
                            'setcl -606298696 "0"\n'
                            'setcl -596600555 "1"\n'
                            'setcl -594746692 "Maximum Performance"\n'
                            'setcl -586472188 "4"\n'
                            'setcl -582520229 "0"\n'
                            'setcl -577841751 "-1"\n'
                            'setcl -529973710 "210"\n'
                            'setcl -491409545 "700"\n'
                            'setcl -446595808 "0.4"\n'
                            'setcl -440385082 "0"\n'
                            'setcl -438689660 "0"\n'
                            'setcl -428383523 "2"\n'
                            'setcl -391139511 "0"\n'
                            'setcl -387906379 "0.022"\n'
                            'setcl -381827765 "auto"\n'
                            'setcl -374150193 "1"\n'
                            'setcl -318730866 "640"\n'
                            'setcl -316446656 "0"\n'
                            'setcl -304904792 "0"\n'
                            'setcl -304821594 "0.25"\n'
                            'setcl -295740762 "0.5"\n'
                            'setcl -293819721 "0.6 0.5 0.6 1"\n'
                            'setcl -286365507 "0.5"\n'
                            'setcl -278540298 "none"\n'
                            'setcl -275786680 "140"\n'
                            'setcl -273510894 "2072.43"\n'
                            'setcl -271879096 "0"\n'
                            'setcl -260307489 "0.0655388"\n'
                            'setcl -247961667 "6000"\n'
                            'setcl -242905693 "3"\n'
                            'setcl -192701482 ""\n'
                            'setcl -178878725 "0.75 0.05"\n'
                            'setcl -166510421 "120"\n'
                            'setcl -153929532 "600"\n'
                            'setcl -151480321 "0.92 0.62"\n'
                            'setcl -125002559 "1"\n'
                            'setcl -114464669 "0"\n'
                            'setcl -103947330 "3"\n'
                            'setcl -88022417 "0"\n'
                            'setcl -46629552 "1"\n'
                            'setcl -45702866 "51179 r511_75"\n'
                            'setcl -43786885 "0.5"\n'
                            'setcl -34753869 "14.004"\n'
                            'setcl -22531807 "1.15"\n'
                            'setcl -8293123 "1"\n'
                        )
                else:
                    tk.messagebox.showinfo('Importante', 'Não abra o jogo em modo de segurança nem dê permissão para o jogo modificar suas configurações gráficas !\n :)')
                    tk.messagebox.showinfo('Importante', 'Selecione o diretório onde se encontra o arquivo de configuração do jogo (Normalmente fica na pasta: Documents\Call of Duty Modern Warfare\players)!\n :)')
                    directory = str(dlg.askdirectory(title='Selecione a configuração'))
                    with open(fr'{directory}\config.cfg', 'w+') as file:
                        file.write(
                            '// generated by KOCKIE to modify kkk\n'
                            'setcl 30049418 "140"\n'
                            'setcl 49997308 "0.5"\n'
                            'setcl 58932476 "S24D332"\n'
                            'setcl 75087430 "1"\n'
                            'setcl 100298170 "200"\n'
                            'setcl 135805301 "0.6"\n'
                            'setcl 174982485 "1.5"\n'
                            'setcl 194177937 "1"\n'
                            'setcl 204768854 "0"\n'
                            'setcl 218404237 "1"\n'
                            'setcl 228392943 "1.5"\n'
                            'setcl 239490324 "1"\n'
                            'setcl 263809092 "0"\n'
                            'setcl 281093946 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 283349319 "12"\n'
                            'setcl 300071733 "0"\n'
                            'setcl 300689787 "0.4749"\n'
                            'setcl 307701044 "0"\n'
                            'setcl 344232750 "1"\n'
                            'setcl 366728169 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 386839215 "0"\n'
                            'setcl 390858914 "0"\n'
                            'setcl 405012731 "1"\n'
                            'setcl 412725085 "1100"\n'
                            'setcl 431324756 "0"\n'
                            'setcl 438033235 "0.75"\n'
                            'setcl 442075206 "0.25"\n'
                            'setcl 452058051 "0"\n'
                            'setcl 459540817 "-1"\n'
                            'setcl 461165839 "1"\n'
                            'setcl 471390880 "0"\n'
                            'setcl 497895430 "-1"\n'
                            'setcl 500533217 "0"\n'
                            'setcl 502072820 "1"\n'
                            'setcl 503885063 "16.11.2"\n'
                            'setcl 506914818 "28"\n'
                            'setcl 524633178 "7"\n'
                            'setcl 530869264 "0.8"\n'
                            'setcl 549656596 "2072.43"\n'
                            'setcl 576994415 "0"\n'
                            'setcl 578190563 "MENU/DEFAULT_COMMUNICATION_DEVICE"\n'
                            'setcl 620032665 "1"\n'
                            'setcl 625258013 "subtitle"\n'
                            'setcl 631512172 "0"\n'
                            'setcl 649200945 "0"\n'
                            'setcl 651190804 "1.5"\n'
                            'setcl 656607832 "0"\n'
                            'setcl 662286220 "1"\n'
                            'setcl 670213830 "1.5"\n'
                            'setcl 683401118 "0"\n'
                            'setcl 695904642 "5"\n'
                            'setcl 728921641 "1"\n'
                            'setcl 741529514 "0"\n'
                            'setcl 763756775 "0.2625"\n'
                            'setcl 834974127 "None"\n'
                            'setcl 870012236 "420"\n'
                            'setcl 875970007 "1"\n'
                            'setcl 876099564 "2"\n'
                            'setcl 880871712 "0"\n'
                            'setcl 895653276 "800x600"\n'
                            'setcl 901605185 "0"\n'
                            'setcl 918242844 "3"\n'
                            'setcl 924246637 "1"\n'
                            'setcl 927356470 "Enabled"\n'
                            'setcl 971698222 "50"\n'
                            'setcl 993324516 "1"\n'
                            'setcl 1010551079 "30"\n'
                            'setcl 1023710916 "mw_default"\n'
                            'setcl 1089030849 "0"\n'
                            'setcl 1112114094 "1000"\n'
                            'setcl 1116474394 "1"\n'
                            'setcl 1120557623 "0.4"\n'
                            'setcl 1178686240 "330"\n'
                            'setcl 1267618646 "1"\n'
                            'setcl 1310823371 "0"\n'
                            'setcl 1389640589 "Off"\n'
                            'setcl 1392059387 "1"\n'
                            'setcl 1414304430 "375.70"\n'
                            'setcl 1429023948 "0.25"\n'
                            'setcl 1445079425 "0.8 0 0 1"\n'
                            'setcl 1455453918 "0"\n'
                            'setcl 1481207725 "1"\n'
                            'setcl 1503870259 "1"\n'
                            'setcl 1503912771 "1"\n'
                            'setcl 1511138344 "400"\n'
                            'setcl 1529983144 "0"\n'
                            'setcl 1539706852 "1"\n'
                            'setcl 1551683251 "1"\n'
                            'setcl 1589004716 "1"\n'
                            'setcl 1595752881 "1"\n'
                            'setcl 1607162157 "Off"\n'
                            'setcl 1612582153 "500"\n'
                            'setcl 1621853845 "-1"\n'
                            'setcl 1635259448 "0.25"\n'
                            'setcl 1649833455 "1"\n'
                            'setcl 1650431234 "75.000"\n'
                            'setcl 1659218611 "3"\n'
                            'setcl 1709018887 "BT709_sRGB"\n'
                            'setcl 1730559565 "-1"\n'
                            'setcl 1741328560 "1"\n'
                            'setcl 1756517702 "2"\n'
                            'setcl 1762842223 "0.5"\n'
                            'setcl 1766991848 "16 11 2"\n'
                            'setcl 1844320632 "1105920"\n'
                            'setcl 1847523626 "Enabled"\n'
                            'setcl 1870423823 "0.25"\n'
                            'setcl 1872772153 "1"\n'
                            'setcl 1878342628 "1"\n'
                            'setcl 1897730391 "0"\n'
                            'setcl 1906772039 "0"\n'
                            'setcl 1912904919 "0 0.6 0.18 1"\n'
                            'setcl 1947817761 "0.55"\n'
                            'setcl 1950622058 "100"\n'
                            'setcl 1959281112 "1.33"\n'
                            'setcl 2037202737 ""\n'
                            'setcl 2058006225 "65536"\n'
                            'setcl 2086828738 "8"\n'
                            'setcl 2107748520 "0.007"\n'
                            'setcl 2122379707 "0"\n'
                            'setcl 2135348401 "0.75"\n'
                            'setcl 2137916686 "0"\n'
                            'setcl 2142502956 "5"\n'
                            'setcl 2144662347 "0.5058"\n'
                            'setcl -2143051707 "1"\n'
                            'setcl -2139668929 "0"\n'
                            'setcl -2137405194 "0"\n'
                            'setcl -2117467049 "1"\n'
                            'setcl -2114644220 "1"\n'
                            'setcl -2105641424 "0"\n'
                            'setcl -2086531702 "0"\n'
                            'setcl -2085697508 "0.25"\n'
                            'setcl -2080133768 "1"\n'
                            'setcl -2074405569 "None"\n'
                            'setcl -2067023712 "1"\n'
                            'setcl -2056187699 "2"\n'
                            'setcl -2034804594 "720"\n'
                            'setcl -2023656898 "0.022"\n'
                            'setcl -2010075995 "TEXTURE_FILTER_NEAREST"\n'
                            'setcl -2002816811 "6"\n'
                            'setcl -1991645855 "5"\n'
                            'setcl -1981625429 "0"\n'
                            'setcl -1972948778 "0.03125 0.01"\n'
                            'setcl -1956509584 "1"\n'
                            'setcl -1955814596 "4.44051"\n'
                            'setcl -1946338041 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl -1915975709 "1"\n'
                            'setcl -1905118811 "5"\n'
                            'setcl -1893739580 "0"\n'
                            'setcl -1891132266 "1"\n'
                            'setcl -1867156735 "1"\n'
                            'setcl -1865705906 "0"\n'
                            'setcl -1842923869 "0.002"\n'
                            'setcl -1835563320 "1"\n'
                            'setcl -1814433719 "0"\n'
                            'setcl -1798389992 "0.25"\n'
                            'setcl -1788235984 "1"\n'
                            'setcl -1781237900 "10 0.1"\n'
                            'setcl -1733029737 "-1"\n'
                            'setcl -1726953279 "10"\n'
                            'setcl -1712782598 "76"\n'
                            'setcl -1700655082 "10"\n'
                            'setcl -1698080106 "1800"\n'
                            'setcl -1684289521 "7.94328"\n'
                            'setcl -1680234015 "1"\n'
                            'setcl -1663250207 "1"\n'
                            'setcl -1650980398 "1.99526"\n'
                            'setcl -1644964340 "1"\n'
                            'setcl -1641719278 "1"\n'
                            'setcl -1635690325 "4"\n'
                            'setcl -1628594889 "1"\n'
                            'setcl -1627085165 "0"\n'
                            'setcl -1588581417 "5"\n'
                            'setcl -1580595131 "0"\n'
                            'setcl -1580591086 "37570"\n'
                            'setcl -1578846674 "2000"\n'
                            'setcl -1557306549 "1"\n'
                            'setcl -1556678412 "-32768"\n'
                            'setcl -1548462097 "0"\n'
                            'setcl -1540799782 "0.4633"\n'
                            'setcl -1534246785 "Off"\n'
                            'setcl -1533549817 "50"\n'
                            'setcl -1500059242 "2"\n'
                            'setcl -1499628353 "120"\n'
                            'setcl -1495716865 "0.4981"\n'
                            'setcl -1492172900 "Fullscreen"\n'
                            'setcl -1485943526 "250"\n'
                            'setcl -1457215672 "Low"\n'
                            'setcl -1440857325 "gamenotify obituary"\n'
                            'setcl -1407078038 "1"\n'
                            'setcl -1403009210 "0.021961 1"\n'
                            'setcl -1340369237 "5"\n'
                            'setcl -1318801789 "0"\n'
                            'setcl -1315502002 "0.00 0.00"\n'
                            'setcl -1308994087 "15"\n'
                            'setcl -1275067384 "-32768"\n'
                            'setcl -1260932940 "1"\n'
                            'setcl -1256506668 ""\n'
                            'setcl -1253873949 "1"\n'
                            'setcl -1243427350 "boldgame"\n'
                            'setcl -1224461919 "1"\n'
                            'setcl -1223963406 "1"\n'
                            'setcl -1202901244 "100"\n'
                            'setcl -1163575897 "mw_default"\n'
                            'setcl -1110058394 "0.8 0.62"\n'
                            'setcl -1096719032 "64"\n'
                            'setcl -1014472453 "1"\n'
                            'setcl -1006049675 "0.25"\n'
                            'setcl -995223359 "0.25"\n'
                            'setcl -992918301 "16.6667"\n'
                            'setcl -967502985 "1"\n'
                            'setcl -951569131 "0"\n'
                            'setcl -918239492 "1"\n'
                            'setcl -903403054 "1"\n'
                            'setcl -871715026 "1"\n'
                            'setcl -869033783 "2"\n'
                            'setcl -860800213 "1"\n'
                            'setcl -826651178 "0.5"\n'
                            'setcl -820249539 "0.8"\n'
                            'setcl -820180432 "2"\n'
                            'setcl -813493907 "0 0.3 0.8 1"\n'
                            'setcl -803409955 "0.25"\n'
                            'setcl -795376234 "1"\n'
                            'setcl -757157143 "1"\n'
                            'setcl -727827321 "0.65"\n'
                            'setcl -726702765 "8129"\n'
                            'setcl -687558011 "1.9"\n'
                            'setcl -653426476 "0_Off"\n'
                            'setcl -652465405 "1"\n'
                            'setcl -641481682 "60"\n'
                            'setcl -623745089 "1"\n'
                            'setcl -616091757 "100"\n'
                            'setcl -606298696 "0"\n'
                            'setcl -596600555 "1"\n'
                            'setcl -594746692 "Maximum Performance"\n'
                            'setcl -586472188 "4"\n'
                            'setcl -582520229 "0"\n'
                            'setcl -577841751 "-1"\n'
                            'setcl -529973710 "210"\n'
                            'setcl -491409545 "700"\n'
                            'setcl -446595808 "0.4"\n'
                            'setcl -440385082 "0"\n'
                            'setcl -438689660 "0"\n'
                            'setcl -428383523 "2"\n'
                            'setcl -391139511 "0"\n'
                            'setcl -387906379 "0.022"\n'
                            'setcl -381827765 "auto"\n'
                            'setcl -374150193 "1"\n'
                            'setcl -318730866 "640"\n'
                            'setcl -316446656 "0"\n'
                            'setcl -304904792 "0"\n'
                            'setcl -304821594 "0.25"\n'
                            'setcl -295740762 "0.5"\n'
                            'setcl -293819721 "0.6 0.5 0.6 1"\n'
                            'setcl -286365507 "0.5"\n'
                            'setcl -278540298 "none"\n'
                            'setcl -275786680 "140"\n'
                            'setcl -273510894 "2072.43"\n'
                            'setcl -271879096 "0"\n'
                            'setcl -260307489 "0.0655388"\n'
                            'setcl -247961667 "6000"\n'
                            'setcl -242905693 "3"\n'
                            'setcl -192701482 ""\n'
                            'setcl -178878725 "0.75 0.05"\n'
                            'setcl -166510421 "120"\n'
                            'setcl -153929532 "600"\n'
                            'setcl -151480321 "0.92 0.62"\n'
                            'setcl -125002559 "1"\n'
                            'setcl -114464669 "0"\n'
                            'setcl -103947330 "3"\n'
                            'setcl -88022417 "0"\n'
                            'setcl -46629552 "1"\n'
                            'setcl -45702866 "51179 r511_75"\n'
                            'setcl -43786885 "0.5"\n'
                            'setcl -34753869 "14.004"\n'
                            'setcl -22531807 "1.15"\n'
                            'setcl -8293123 "1"\n'
                        )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi criada com sucesso !\n :)')
            elif varchk.get() == 5:
                if os.path.isdir(f"C:/Users/{user}/Documents/Call of Duty Modern Warfare/players"):
                    tk.messagebox.showinfo('Importante', 'Não abra o jogo em modo de segurança nem dê permissão para o jogo modificar suas configurações gráficas !\n :)')
                    with open(fr'C:\Users\{user}\Documents\Call of Duty Modern Warfare\players\config.cfg', 'w+') as file:
                        file.write(
                            '// generated by KOCKIE to modify kkk\n'
                            'setcl 30049418 "140"\n'
                            'setcl 49997308 "0.5"\n'
                            'setcl 58932476 "S24D332"\n'
                            'setcl 75087430 "1"\n'
                            'setcl 100298170 "200"\n'
                            'setcl 135805301 "0.6"\n'
                            'setcl 174982485 "1.5"\n'
                            'setcl 194177937 "1"\n'
                            'setcl 204768854 "0"\n'
                            'setcl 218404237 "1"\n'
                            'setcl 228392943 "1.5"\n'
                            'setcl 239490324 "1"\n'
                            'setcl 263809092 "0"\n'
                            'setcl 281093946 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 283349319 "12"\n'
                            'setcl 300071733 "0"\n'
                            'setcl 300689787 "0.4749"\n'
                            'setcl 307701044 "0"\n'
                            'setcl 344232750 "1"\n'
                            'setcl 366728169 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 386839215 "0"\n'
                            'setcl 390858914 "0"\n'
                            'setcl 405012731 "1"\n'
                            'setcl 412725085 "1100"\n'
                            'setcl 431324756 "0"\n'
                            'setcl 438033235 "0.75"\n'
                            'setcl 442075206 "0.25"\n'
                            'setcl 452058051 "0"\n'
                            'setcl 459540817 "-1"\n'
                            'setcl 461165839 "1"\n'
                            'setcl 471390880 "0"\n'
                            'setcl 497895430 "-1"\n'
                            'setcl 500533217 "0"\n'
                            'setcl 502072820 "1"\n'
                            'setcl 503885063 "16.11.2"\n'
                            'setcl 506914818 "28"\n'
                            'setcl 524633178 "7"\n'
                            'setcl 530869264 "0.8"\n'
                            'setcl 549656596 "2072.43"\n'
                            'setcl 576994415 "0"\n'
                            'setcl 578190563 "MENU/DEFAULT_COMMUNICATION_DEVICE"\n'
                            'setcl 620032665 "1"\n'
                            'setcl 625258013 "subtitle"\n'
                            'setcl 631512172 "0"\n'
                            'setcl 649200945 "0"\n'
                            'setcl 651190804 "1.5"\n'
                            'setcl 656607832 "0"\n'
                            'setcl 662286220 "1"\n'
                            'setcl 670213830 "1.5"\n'
                            'setcl 683401118 "0"\n'
                            'setcl 695904642 "5"\n'
                            'setcl 728921641 "1"\n'
                            'setcl 741529514 "0"\n'
                            'setcl 763756775 "0.2625"\n'
                            'setcl 834974127 "SMAA 1x"\n'
                            'setcl 870012236 "420"\n'
                            'setcl 875970007 "1"\n'
                            'setcl 876099564 "2"\n'
                            'setcl 880871712 "0"\n'
                            'setcl 895653276 "1920x1080"\n'
                            'setcl 901605185 "0"\n'
                            'setcl 918242844 "3"\n'
                            'setcl 924246637 "1"\n'
                            'setcl 927356470 "Enabled"\n'
                            'setcl 971698222 "50"\n'
                            'setcl 993324516 "1"\n'
                            'setcl 1010551079 "30"\n'
                            'setcl 1023710916 "mw_default"\n'
                            'setcl 1089030849 "0"\n'
                            'setcl 1112114094 "1000"\n'
                            'setcl 1116474394 "1"\n'
                            'setcl 1120557623 "0.4"\n'
                            'setcl 1178686240 "330"\n'
                            'setcl 1267618646 "1"\n'
                            'setcl 1310823371 "0"\n'
                            'setcl 1389640589 "Off"\n'
                            'setcl 1392059387 "1"\n'
                            'setcl 1414304430 "375.70"\n'
                            'setcl 1429023948 "0.25"\n'
                            'setcl 1445079425 "0.8 0 0 1"\n'
                            'setcl 1455453918 "0"\n'
                            'setcl 1481207725 "1"\n'
                            'setcl 1503870259 "1"\n'
                            'setcl 1503912771 "1"\n'
                            'setcl 1511138344 "400"\n'
                            'setcl 1529983144 "0"\n'
                            'setcl 1539706852 "1"\n'
                            'setcl 1551683251 "1"\n'
                            'setcl 1589004716 "1"\n'
                            'setcl 1595752881 "1"\n'
                            'setcl 1607162157 "Off"\n'
                            'setcl 1612582153 "500"\n'
                            'setcl 1621853845 "-1"\n'
                            'setcl 1635259448 "0.25"\n'
                            'setcl 1649833455 "1"\n'
                            'setcl 1650431234 "74.973"\n'
                            'setcl 1659218611 "3"\n'
                            'setcl 1709018887 "BT709_sRGB"\n'
                            'setcl 1730559565 "-1"\n'
                            'setcl 1741328560 "1"\n'
                            'setcl 1756517702 "2"\n'
                            'setcl 1762842223 "0.5"\n'
                            'setcl 1766991848 "16 11 2"\n'
                            'setcl 1844320632 "1105920"\n'
                            'setcl 1847523626 "Enabled"\n'
                            'setcl 1870423823 "0.25"\n'
                            'setcl 1872772153 "1"\n'
                            'setcl 1878342628 "1"\n'
                            'setcl 1897730391 "0"\n'
                            'setcl 1906772039 "0"\n'
                            'setcl 1912904919 "0 0.6 0.18 1"\n'
                            'setcl 1947817761 "0.55"\n'
                            'setcl 1950622058 "100"\n'
                            'setcl 1959281112 "1.33"\n'
                            'setcl 2037202737 ""\n'
                            'setcl 2058006225 "65536"\n'
                            'setcl 2086828738 "8"\n'
                            'setcl 2107748520 "0.007"\n'
                            'setcl 2122379707 "0"\n'
                            'setcl 2135348401 "0.75"\n'
                            'setcl 2137916686 "0"\n'
                            'setcl 2142502956 "5"\n'
                            'setcl 2144662347 "0.5058"\n'
                            'setcl -2143051707 "1"\n'
                            'setcl -2139668929 "0"\n'
                            'setcl -2137405194 "0"\n'
                            'setcl -2117467049 "1"\n'
                            'setcl -2114644220 "1"\n'
                            'setcl -2105641424 "0"\n'
                            'setcl -2086531702 "0"\n'
                            'setcl -2085697508 "0.25"\n'
                            'setcl -2080133768 "1"\n'
                            'setcl -2074405569 "SMAA 1x"\n'
                            'setcl -2067023712 "1"\n'
                            'setcl -2056187699 "2"\n'
                            'setcl -2034804594 "720"\n'
                            'setcl -2023656898 "0.022"\n'
                            'setcl -2010075995 "TEXTURE_FILTER_NEAREST"\n'
                            'setcl -2002816811 "6"\n'
                            'setcl -1991645855 "5"\n'
                            'setcl -1981625429 "0"\n'
                            'setcl -1972948778 "0.03125 0.01"\n'
                            'setcl -1956509584 "1"\n'
                            'setcl -1955814596 "4.44051"\n'
                            'setcl -1946338041 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl -1915975709 "1"\n'
                            'setcl -1905118811 "5"\n'
                            'setcl -1893739580 "0"\n'
                            'setcl -1891132266 "1"\n'
                            'setcl -1867156735 "1"\n'
                            'setcl -1865705906 "0"\n'
                            'setcl -1842923869 "0.002"\n'
                            'setcl -1835563320 "1"\n'
                            'setcl -1814433719 "0"\n'
                            'setcl -1798389992 "0.25"\n'
                            'setcl -1788235984 "1"\n'
                            'setcl -1781237900 "10 0.1"\n'
                            'setcl -1733029737 "-1"\n'
                            'setcl -1726953279 "10"\n'
                            'setcl -1712782598 "80"\n'
                            'setcl -1700655082 "10"\n'
                            'setcl -1698080106 "1800"\n'
                            'setcl -1684289521 "7.94328"\n'
                            'setcl -1680234015 "1"\n'
                            'setcl -1663250207 "1"\n'
                            'setcl -1650980398 "1.99526"\n'
                            'setcl -1644964340 "1"\n'
                            'setcl -1641719278 "1"\n'
                            'setcl -1635690325 "4"\n'
                            'setcl -1628594889 "1"\n'
                            'setcl -1627085165 "0"\n'
                            'setcl -1588581417 "5"\n'
                            'setcl -1580595131 "0"\n'
                            'setcl -1580591086 "37570"\n'
                            'setcl -1578846674 "2000"\n'
                            'setcl -1557306549 "1"\n'
                            'setcl -1556678412 "-32768"\n'
                            'setcl -1548462097 "0"\n'
                            'setcl -1540799782 "0.4633"\n'
                            'setcl -1534246785 "Off"\n'
                            'setcl -1533549817 "50"\n'
                            'setcl -1500059242 "2"\n'
                            'setcl -1499628353 "120"\n'
                            'setcl -1495716865 "0.4981"\n'
                            'setcl -1492172900 "Fullscreen"\n'
                            'setcl -1485943526 "250"\n'
                            'setcl -1457215672 "Normal"\n'
                            'setcl -1440857325 "gamenotify obituary"\n'
                            'setcl -1407078038 "1"\n'
                            'setcl -1403009210 "0.021961 1"\n'
                            'setcl -1340369237 "5"\n'
                            'setcl -1318801789 "0"\n'
                            'setcl -1315502002 "0.00 0.00"\n'
                            'setcl -1308994087 "15"\n'
                            'setcl -1275067384 "-32768"\n'
                            'setcl -1260932940 "1"\n'
                            'setcl -1256506668 ""\n'
                            'setcl -1253873949 "1"\n'
                            'setcl -1243427350 "boldgame"\n'
                            'setcl -1224461919 "1"\n'
                            'setcl -1223963406 "1"\n'
                            'setcl -1202901244 "100"\n'
                            'setcl -1163575897 "mw_default"\n'
                            'setcl -1110058394 "0.8 0.62"\n'
                            'setcl -1096719032 "64"\n'
                            'setcl -1014472453 "1"\n'
                            'setcl -1006049675 "0.25"\n'
                            'setcl -995223359 "0.25"\n'
                            'setcl -992918301 "16.6667"\n'
                            'setcl -967502985 "1"\n'
                            'setcl -951569131 "0"\n'
                            'setcl -918239492 "1"\n'
                            'setcl -903403054 "1"\n'
                            'setcl -871715026 "1"\n'
                            'setcl -869033783 "2"\n'
                            'setcl -860800213 "1"\n'
                            'setcl -826651178 "0.5"\n'
                            'setcl -820249539 "0.8"\n'
                            'setcl -820180432 "2"\n'
                            'setcl -813493907 "0 0.3 0.8 1"\n'
                            'setcl -803409955 "0.25"\n'
                            'setcl -795376234 "1"\n'
                            'setcl -757157143 "1"\n'
                            'setcl -727827321 "0.65"\n'
                            'setcl -726702765 "8129"\n'
                            'setcl -687558011 "1.9"\n'
                            'setcl -653426476 "0_Off"\n'
                            'setcl -652465405 "1"\n'
                            'setcl -641481682 "60"\n'
                            'setcl -623745089 "1"\n'
                            'setcl -616091757 "100"\n'
                            'setcl -606298696 "0"\n'
                            'setcl -596600555 "1"\n'
                            'setcl -594746692 "Maximum Performance"\n'
                            'setcl -586472188 "4"\n'
                            'setcl -582520229 "0"\n'
                            'setcl -577841751 "-1"\n'
                            'setcl -529973710 "210"\n'
                            'setcl -491409545 "700"\n'
                            'setcl -446595808 "0.4"\n'
                            'setcl -440385082 "0"\n'
                            'setcl -438689660 "0"\n'
                            'setcl -428383523 "2"\n'
                            'setcl -391139511 "0"\n'
                            'setcl -387906379 "0.022"\n'
                            'setcl -381827765 "auto"\n'
                            'setcl -374150193 "1"\n'
                            'setcl -318730866 "640"\n'
                            'setcl -316446656 "1"\n'
                            'setcl -304904792 "0"\n'
                            'setcl -304821594 "0.25"\n'
                            'setcl -295740762 "0.5"\n'
                            'setcl -293819721 "0.6 0.5 0.6 1"\n'
                            'setcl -286365507 "0.5"\n'
                            'setcl -278540298 "none"\n'
                            'setcl -275786680 "140"\n'
                            'setcl -273510894 "2072.43"\n'
                            'setcl -271879096 "0"\n'
                            'setcl -260307489 "0.0655388"\n'
                            'setcl -247961667 "6000"\n'
                            'setcl -242905693 "3"\n'
                            'setcl -192701482 ""\n'
                            'setcl -178878725 "0.75 0.05"\n'
                            'setcl -166510421 "120"\n'
                            'setcl -153929532 "600"\n'
                            'setcl -151480321 "0.92 0.62"\n'
                            'setcl -125002559 "1"\n'
                            'setcl -114464669 "0"\n'
                            'setcl -103947330 "3"\n'
                            'setcl -88022417 "0"\n'
                            'setcl -46629552 "1"\n'
                            'setcl -45702866 "51179 r511_75"\n'
                            'setcl -43786885 "0.5"\n'
                            'setcl -34753869 "14.004"\n'
                            'setcl -22531807 "1.15"\n'
                            'setcl -8293123 "1"\n'
                        )
                else:
                    tk.messagebox.showinfo('Importante', 'Não abra o jogo em modo de segurança nem dê permissão para o jogo modificar suas configurações gráficas !\n :)')
                    tk.messagebox.showinfo('Importante', 'Selecione o diretório onde se encontra o arquivo de configuração do jogo (Normalmente fica na pasta: Documents\Call of Duty Modern Warfare\players)!\n :)')
                    directory = str(dlg.askdirectory(title='Selecione a configuração'))
                    with open(fr'{directory}\config.cfg', 'w+') as file:
                        file.write(
                            '// generated by KOCKIE to modify kkk\n'
                            'setcl 30049418 "140"\n'
                            'setcl 49997308 "0.5"\n'
                            'setcl 58932476 "S24D332"\n'
                            'setcl 75087430 "1"\n'
                            'setcl 100298170 "200"\n'
                            'setcl 135805301 "0.6"\n'
                            'setcl 174982485 "1.5"\n'
                            'setcl 194177937 "1"\n'
                            'setcl 204768854 "0"\n'
                            'setcl 218404237 "1"\n'
                            'setcl 228392943 "1.5"\n'
                            'setcl 239490324 "1"\n'
                            'setcl 263809092 "0"\n'
                            'setcl 281093946 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 283349319 "12"\n'
                            'setcl 300071733 "0"\n'
                            'setcl 300689787 "0.4749"\n'
                            'setcl 307701044 "0"\n'
                            'setcl 344232750 "1"\n'
                            'setcl 366728169 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl 386839215 "0"\n'
                            'setcl 390858914 "0"\n'
                            'setcl 405012731 "1"\n'
                            'setcl 412725085 "1100"\n'
                            'setcl 431324756 "0"\n'
                            'setcl 438033235 "0.75"\n'
                            'setcl 442075206 "0.25"\n'
                            'setcl 452058051 "0"\n'
                            'setcl 459540817 "-1"\n'
                            'setcl 461165839 "1"\n'
                            'setcl 471390880 "0"\n'
                            'setcl 497895430 "-1"\n'
                            'setcl 500533217 "0"\n'
                            'setcl 502072820 "1"\n'
                            'setcl 503885063 "16.11.2"\n'
                            'setcl 506914818 "28"\n'
                            'setcl 524633178 "7"\n'
                            'setcl 530869264 "0.8"\n'
                            'setcl 549656596 "2072.43"\n'
                            'setcl 576994415 "0"\n'
                            'setcl 578190563 "MENU/DEFAULT_COMMUNICATION_DEVICE"\n'
                            'setcl 620032665 "1"\n'
                            'setcl 625258013 "subtitle"\n'
                            'setcl 631512172 "0"\n'
                            'setcl 649200945 "0"\n'
                            'setcl 651190804 "1.5"\n'
                            'setcl 656607832 "0"\n'
                            'setcl 662286220 "1"\n'
                            'setcl 670213830 "1.5"\n'
                            'setcl 683401118 "0"\n'
                            'setcl 695904642 "5"\n'
                            'setcl 728921641 "1"\n'
                            'setcl 741529514 "0"\n'
                            'setcl 763756775 "0.2625"\n'
                            'setcl 834974127 "SMAA 1x"\n'
                            'setcl 870012236 "420"\n'
                            'setcl 875970007 "1"\n'
                            'setcl 876099564 "2"\n'
                            'setcl 880871712 "0"\n'
                            'setcl 895653276 "1920x1080"\n'
                            'setcl 901605185 "0"\n'
                            'setcl 918242844 "3"\n'
                            'setcl 924246637 "1"\n'
                            'setcl 927356470 "Enabled"\n'
                            'setcl 971698222 "50"\n'
                            'setcl 993324516 "1"\n'
                            'setcl 1010551079 "30"\n'
                            'setcl 1023710916 "mw_default"\n'
                            'setcl 1089030849 "0"\n'
                            'setcl 1112114094 "1000"\n'
                            'setcl 1116474394 "1"\n'
                            'setcl 1120557623 "0.4"\n'
                            'setcl 1178686240 "330"\n'
                            'setcl 1267618646 "1"\n'
                            'setcl 1310823371 "0"\n'
                            'setcl 1389640589 "Off"\n'
                            'setcl 1392059387 "1"\n'
                            'setcl 1414304430 "375.70"\n'
                            'setcl 1429023948 "0.25"\n'
                            'setcl 1445079425 "0.8 0 0 1"\n'
                            'setcl 1455453918 "0"\n'
                            'setcl 1481207725 "1"\n'
                            'setcl 1503870259 "1"\n'
                            'setcl 1503912771 "1"\n'
                            'setcl 1511138344 "400"\n'
                            'setcl 1529983144 "0"\n'
                            'setcl 1539706852 "1"\n'
                            'setcl 1551683251 "1"\n'
                            'setcl 1589004716 "1"\n'
                            'setcl 1595752881 "1"\n'
                            'setcl 1607162157 "Off"\n'
                            'setcl 1612582153 "500"\n'
                            'setcl 1621853845 "-1"\n'
                            'setcl 1635259448 "0.25"\n'
                            'setcl 1649833455 "1"\n'
                            'setcl 1650431234 "74.973"\n'
                            'setcl 1659218611 "3"\n'
                            'setcl 1709018887 "BT709_sRGB"\n'
                            'setcl 1730559565 "-1"\n'
                            'setcl 1741328560 "1"\n'
                            'setcl 1756517702 "2"\n'
                            'setcl 1762842223 "0.5"\n'
                            'setcl 1766991848 "16 11 2"\n'
                            'setcl 1844320632 "1105920"\n'
                            'setcl 1847523626 "Enabled"\n'
                            'setcl 1870423823 "0.25"\n'
                            'setcl 1872772153 "1"\n'
                            'setcl 1878342628 "1"\n'
                            'setcl 1897730391 "0"\n'
                            'setcl 1906772039 "0"\n'
                            'setcl 1912904919 "0 0.6 0.18 1"\n'
                            'setcl 1947817761 "0.55"\n'
                            'setcl 1950622058 "100"\n'
                            'setcl 1959281112 "1.33"\n'
                            'setcl 2037202737 ""\n'
                            'setcl 2058006225 "65536"\n'
                            'setcl 2086828738 "8"\n'
                            'setcl 2107748520 "0.007"\n'
                            'setcl 2122379707 "0"\n'
                            'setcl 2135348401 "0.75"\n'
                            'setcl 2137916686 "0"\n'
                            'setcl 2142502956 "5"\n'
                            'setcl 2144662347 "0.5058"\n'
                            'setcl -2143051707 "1"\n'
                            'setcl -2139668929 "0"\n'
                            'setcl -2137405194 "0"\n'
                            'setcl -2117467049 "1"\n'
                            'setcl -2114644220 "1"\n'
                            'setcl -2105641424 "0"\n'
                            'setcl -2086531702 "0"\n'
                            'setcl -2085697508 "0.25"\n'
                            'setcl -2080133768 "1"\n'
                            'setcl -2074405569 "SMAA 1x"\n'
                            'setcl -2067023712 "1"\n'
                            'setcl -2056187699 "2"\n'
                            'setcl -2034804594 "720"\n'
                            'setcl -2023656898 "0.022"\n'
                            'setcl -2010075995 "TEXTURE_FILTER_NEAREST"\n'
                            'setcl -2002816811 "6"\n'
                            'setcl -1991645855 "5"\n'
                            'setcl -1981625429 "0"\n'
                            'setcl -1972948778 "0.03125 0.01"\n'
                            'setcl -1956509584 "1"\n'
                            'setcl -1955814596 "4.44051"\n'
                            'setcl -1946338041 "{0.0.0.00000000}.{BC46A4FD-F2D8-4E74-85F7-0C70BF3313A2}"\n'
                            'setcl -1915975709 "1"\n'
                            'setcl -1905118811 "5"\n'
                            'setcl -1893739580 "0"\n'
                            'setcl -1891132266 "1"\n'
                            'setcl -1867156735 "1"\n'
                            'setcl -1865705906 "0"\n'
                            'setcl -1842923869 "0.002"\n'
                            'setcl -1835563320 "1"\n'
                            'setcl -1814433719 "0"\n'
                            'setcl -1798389992 "0.25"\n'
                            'setcl -1788235984 "1"\n'
                            'setcl -1781237900 "10 0.1"\n'
                            'setcl -1733029737 "-1"\n'
                            'setcl -1726953279 "10"\n'
                            'setcl -1712782598 "80"\n'
                            'setcl -1700655082 "10"\n'
                            'setcl -1698080106 "1800"\n'
                            'setcl -1684289521 "7.94328"\n'
                            'setcl -1680234015 "1"\n'
                            'setcl -1663250207 "1"\n'
                            'setcl -1650980398 "1.99526"\n'
                            'setcl -1644964340 "1"\n'
                            'setcl -1641719278 "1"\n'
                            'setcl -1635690325 "4"\n'
                            'setcl -1628594889 "1"\n'
                            'setcl -1627085165 "0"\n'
                            'setcl -1588581417 "5"\n'
                            'setcl -1580595131 "0"\n'
                            'setcl -1580591086 "37570"\n'
                            'setcl -1578846674 "2000"\n'
                            'setcl -1557306549 "1"\n'
                            'setcl -1556678412 "-32768"\n'
                            'setcl -1548462097 "0"\n'
                            'setcl -1540799782 "0.4633"\n'
                            'setcl -1534246785 "Off"\n'
                            'setcl -1533549817 "50"\n'
                            'setcl -1500059242 "2"\n'
                            'setcl -1499628353 "120"\n'
                            'setcl -1495716865 "0.4981"\n'
                            'setcl -1492172900 "Fullscreen"\n'
                            'setcl -1485943526 "250"\n'
                            'setcl -1457215672 "Normal"\n'
                            'setcl -1440857325 "gamenotify obituary"\n'
                            'setcl -1407078038 "1"\n'
                            'setcl -1403009210 "0.021961 1"\n'
                            'setcl -1340369237 "5"\n'
                            'setcl -1318801789 "0"\n'
                            'setcl -1315502002 "0.00 0.00"\n'
                            'setcl -1308994087 "15"\n'
                            'setcl -1275067384 "-32768"\n'
                            'setcl -1260932940 "1"\n'
                            'setcl -1256506668 ""\n'
                            'setcl -1253873949 "1"\n'
                            'setcl -1243427350 "boldgame"\n'
                            'setcl -1224461919 "1"\n'
                            'setcl -1223963406 "1"\n'
                            'setcl -1202901244 "100"\n'
                            'setcl -1163575897 "mw_default"\n'
                            'setcl -1110058394 "0.8 0.62"\n'
                            'setcl -1096719032 "64"\n'
                            'setcl -1014472453 "1"\n'
                            'setcl -1006049675 "0.25"\n'
                            'setcl -995223359 "0.25"\n'
                            'setcl -992918301 "16.6667"\n'
                            'setcl -967502985 "1"\n'
                            'setcl -951569131 "0"\n'
                            'setcl -918239492 "1"\n'
                            'setcl -903403054 "1"\n'
                            'setcl -871715026 "1"\n'
                            'setcl -869033783 "2"\n'
                            'setcl -860800213 "1"\n'
                            'setcl -826651178 "0.5"\n'
                            'setcl -820249539 "0.8"\n'
                            'setcl -820180432 "2"\n'
                            'setcl -813493907 "0 0.3 0.8 1"\n'
                            'setcl -803409955 "0.25"\n'
                            'setcl -795376234 "1"\n'
                            'setcl -757157143 "1"\n'
                            'setcl -727827321 "0.65"\n'
                            'setcl -726702765 "8129"\n'
                            'setcl -687558011 "1.9"\n'
                            'setcl -653426476 "0_Off"\n'
                            'setcl -652465405 "1"\n'
                            'setcl -641481682 "60"\n'
                            'setcl -623745089 "1"\n'
                            'setcl -616091757 "100"\n'
                            'setcl -606298696 "0"\n'
                            'setcl -596600555 "1"\n'
                            'setcl -594746692 "Maximum Performance"\n'
                            'setcl -586472188 "4"\n'
                            'setcl -582520229 "0"\n'
                            'setcl -577841751 "-1"\n'
                            'setcl -529973710 "210"\n'
                            'setcl -491409545 "700"\n'
                            'setcl -446595808 "0.4"\n'
                            'setcl -440385082 "0"\n'
                            'setcl -438689660 "0"\n'
                            'setcl -428383523 "2"\n'
                            'setcl -391139511 "0"\n'
                            'setcl -387906379 "0.022"\n'
                            'setcl -381827765 "auto"\n'
                            'setcl -374150193 "1"\n'
                            'setcl -318730866 "640"\n'
                            'setcl -316446656 "1"\n'
                            'setcl -304904792 "0"\n'
                            'setcl -304821594 "0.25"\n'
                            'setcl -295740762 "0.5"\n'
                            'setcl -293819721 "0.6 0.5 0.6 1"\n'
                            'setcl -286365507 "0.5"\n'
                            'setcl -278540298 "none"\n'
                            'setcl -275786680 "140"\n'
                            'setcl -273510894 "2072.43"\n'
                            'setcl -271879096 "0"\n'
                            'setcl -260307489 "0.0655388"\n'
                            'setcl -247961667 "6000"\n'
                            'setcl -242905693 "3"\n'
                            'setcl -192701482 ""\n'
                            'setcl -178878725 "0.75 0.05"\n'
                            'setcl -166510421 "120"\n'
                            'setcl -153929532 "600"\n'
                            'setcl -151480321 "0.92 0.62"\n'
                            'setcl -125002559 "1"\n'
                            'setcl -114464669 "0"\n'
                            'setcl -103947330 "3"\n'
                            'setcl -88022417 "0"\n'
                            'setcl -46629552 "1"\n'
                            'setcl -45702866 "51179 r511_75"\n'
                            'setcl -43786885 "0.5"\n'
                            'setcl -34753869 "14.004"\n'
                            'setcl -22531807 "1.15"\n'
                            'setcl -8293123 "1"\n'
                        )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi substituída com sucesso !\n :)')
        except:
            tk.messagebox.showerror('Erro', 'Não foi possível modificar sua configuração, o jogo ou a configuração não foi encontrado(a) no sistema !\n :(')

    def btnValorantAction():
        try:
            if varchk.get() == 6:
                tk.messagebox.showinfo('Importante', 'Selecione no diretório já aberto, onde se encontra o arquivo de configuração do jogo (Normalmente se encontra na pasta "Windows" que está dentro de uma pasta cujo nome é aleatório)!\n :)')
                directory = str(dlg.askdirectory(title='Selecione a configuração', initialdir=(f'C:/Users/{user}/AppData/Local/VALORANT/Saved/Config')))
                with open(fr'{directory}\RiotUserSettings.ini', 'w+') as file:
                    file.write(
                        '[Settings]\n'
                        'LocalSettingsVersion=6\n'
                        'EAresStringSettingName::CrosshairProfileName=Kockiee\n'
                        'EAresBoolSettingName::HasSeenSettingsTutorial=True\n'
                        'EAresBoolSettingName::HasSeenPhotoSensitivityWarning=True\n'
                        'EAresBoolSettingName::HasEverAppliedRoamingSettings=True\n'
                        'EAresStringSettingName::LastSeenSeasonalPopup=episode4act\n2'
                        'EAresBoolSettingName::DisableDistortion=False\n'
                        'EAresBoolSettingName::ShadowsEnabled=False\n'
                        'EAresIntSettingName::MaterialQuality=0\n'
                        'EAresIntSettingName::TextureQuality=0\n'
                        'EAresIntSettingName::DetailQuality=0\n'
                        'EAresIntSettingName::UIQuality=0\n'
                        'EAresIntSettingName::BloomQuality=0\n'
                        'EAresBoolSettingName::ImproveClarity=True'
                    )
                with open(fr'{directory}\GameUserSettings.ini', 'w+') as file:
                    file.write(
                        '[/Script/ShooterGame.ShooterGameUserSettings]\n'
                        'DefaultMonitorDeviceID="MONITOR\\SAM0F5E\\{4d36e96e-e325-11ce-bfc1-08002be10318}\\0002"\n'
                        'DefaultMonitorIndex=0\n'
                        'LastConfirmedDefaultMonitorDeviceID="MONITOR\\SAM0F5E\\{4d36e96e-e325-11ce-bfc1-08002be10318}\\0002"\n'
                        'LastConfirmedDefaultMonitorIndex=0\n'
                        'bShouldLetterbox=True\n'
                        'bLastConfirmedShouldLetterbox=True\n'
                        'bUseVSync=False\n'
                        'bUseDynamicResolution=False\n'
                        'ResolutionSizeX=1920\n'
                        'ResolutionSizeY=1080\n'
                        'LastUserConfirmedResolutionSizeX=1920\n'
                        'LastUserConfirmedResolutionSizeY=1080\n'
                        'WindowPosX=0\n'
                        'WindowPosY=0\n'
                        'LastConfirmedFullscreenMode=0\n'
                        'PreferredFullscreenMode=1\n'
                        'AudioQualityLevel=0\n'
                        'LastConfirmedAudioQualityLevel=0\n'
                        'FrameRateLimit=0.000000\n'
                        'DesiredScreenWidth=1280\n'
                        'DesiredScreenHeight=720\n'
                        'LastUserConfirmedDesiredScreenWidth=1280\n'
                        'LastUserConfirmedDesiredScreenHeight=720\n'
                        'LastRecommendedScreenWidth=-1.000000\n'
                        'LastRecommendedScreenHeight=-1.000000\n'
                        'LastCPUBenchmarkResult=-1.000000\n'
                        'LastGPUBenchmarkResult=-1.000000\n'
                        'LastGPUBenchmarkMultiplier=1.000000\n'
                        'bUseHDRDisplayOutput=False\n'
                        'HDRDisplayOutputNits=1000\n'
                        '\n'
                        '[/Script/Engine.GameUserSettings]\n'
                        'bUseDesiredScreenHeight=False\n'
                        '\n'
                        '[ScalabilityGroups]\n'
                        'sg.ResolutionQuality=75.000000\n'
                        'sg.ViewDistanceQuality=2\n'
                        'sg.AntiAliasingQuality=0\n'
                        'sg.ShadowQuality=0\n'
                        'sg.PostProcessQuality=0\n'
                        'sg.TextureQuality=0\n'
                        'sg.EffectsQuality=0\n'
                        'sg.FoliageQuality=0\n'
                        'sg.ShadingQuality=0\n'
                        '\n'
                        '[ShaderPipelineCache.CacheFile]\n'
                        'LastOpened=ShooterGame\n'
                    )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi substituída com sucesso !\n :)')
            elif varchk.get() == 7:
                tk.messagebox.showinfo('Importante', 'Selecione no diretório já aberto, onde se encontra o arquivo de configuração do jogo (Normalmente se encontra na pasta "Windows" que está dentro de uma pasta cujo nome é aleatório)!\n :)')
                directory = str(dlg.askdirectory(title='Selecione a configuração', initialdir=(f'C:/Users/{user}/AppData/Local/VALORANT/Saved/Config')))
                with open(fr'{directory}\RiotUserSettings.ini', 'w+') as file:
                    file.write(
                        '[Settings]\n'
                        'LocalSettingsVersion=6\n'
                        'EAresStringSettingName::CrosshairProfileName=Kockiee\n'
                        'EAresBoolSettingName::HasSeenSettingsTutorial=True\n'
                        'EAresBoolSettingName::HasSeenPhotoSensitivityWarning=True\n'
                        'EAresBoolSettingName::HasEverAppliedRoamingSettings=True\n'
                        'EAresStringSettingName::LastSeenSeasonalPopup=episode4act2\n'
                        'EAresBoolSettingName::DisableDistortion=False\n'
                        'EAresBoolSettingName::ShadowsEnabled=False\n'
                        'EAresIntSettingName::MaterialQuality=0\n'
                        'EAresIntSettingName::TextureQuality=0\n'
                        'EAresIntSettingName::DetailQuality=1\n'
                        'EAresIntSettingName::UIQuality=0\n'
                        'EAresIntSettingName::BloomQuality=0\n'
                        'EAresBoolSettingName::ImproveClarity=True'
                    )
                with open(fr'{directory}\GameUserSettings.ini', 'w+') as file:
                    file.write(
                        '[/Script/ShooterGame.ShooterGameUserSettings]\n'
                        'DefaultMonitorDeviceID="MONITOR\\SAM0F5E\\{4d36e96e-e325-11ce-bfc1-08002be10318}\\0002"\n'
                        'DefaultMonitorIndex=0\n'
                        'LastConfirmedDefaultMonitorDeviceID="MONITOR\\SAM0F5E\\{4d36e96e-e325-11ce-bfc1-08002be10318}\\0002"\n'
                        'LastConfirmedDefaultMonitorIndex=0\n'
                        'bShouldLetterbox=True\n'
                        'bLastConfirmedShouldLetterbox=True\n'
                        'bUseVSync=False\n'
                        'bUseDynamicResolution=False\n'
                        'ResolutionSizeX=1920\n'
                        'ResolutionSizeY=1080\n'
                        'LastUserConfirmedResolutionSizeX=1920\n'
                        'LastUserConfirmedResolutionSizeY=1080\n'
                        'WindowPosX=0\n'
                        'WindowPosY=0\n'
                        'LastConfirmedFullscreenMode=0\n'
                        'PreferredFullscreenMode=1\n'
                        'AudioQualityLevel=0\n'
                        'LastConfirmedAudioQualityLevel=0\n'
                        'FrameRateLimit=0.000000\n'
                        'DesiredScreenWidth=1280\n'
                        'DesiredScreenHeight=720\n'
                        'LastUserConfirmedDesiredScreenWidth=1280\n'
                        'LastUserConfirmedDesiredScreenHeight=720\n'
                        'LastRecommendedScreenWidth=-1.000000\n'
                        'LastRecommendedScreenHeight=-1.000000\n'
                        'LastCPUBenchmarkResult=-1.000000\n'
                        'LastGPUBenchmarkResult=-1.000000\n'
                        'LastGPUBenchmarkMultiplier=1.000000\n'
                        'bUseHDRDisplayOutput=False\n'
                        'HDRDisplayOutputNits=1000\n'
                        '\n'
                        '[/Script/Engine.GameUserSettings]\n'
                        'bUseDesiredScreenHeight=False\n'
                        '\n'
                        '[ScalabilityGroups]\n'
                        'sg.ResolutionQuality=85.000000\n'
                        'sg.ViewDistanceQuality=3\n'
                        'sg.AntiAliasingQuality=0\n'
                        'sg.ShadowQuality=0\n'
                        'sg.PostProcessQuality=0\n'
                        'sg.TextureQuality=0\n'
                        'sg.EffectsQuality=0\n'
                        'sg.FoliageQuality=0\n'
                        'sg.ShadingQuality=0\n'
                        '\n'
                        '[ShaderPipelineCache.CacheFile]\n'
                        'LastOpened=ShooterGame\n'
                    )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi substituída com sucesso !\n :)')
        except:
            tk.messagebox.showerror('Erro', 'Não foi possível modificar sua configuração, o jogo ou a configuração não foi encontrado(a) no sistema !\n :(')

    def btnCSGOAction():
        try:
            tk.messagebox.showinfo('Importante', 'Após a modificação ser concluída, vá para as propriedades do jogo (na Steam) e nas opções de inicialização, adicione a seguinte linha de comando: +exec boost.cfg')
            if varchk.get() == 8:
                with open(fr'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\boost.cfg', 'w+') as file:
                    file.write(
                        'fps_max 0\n'
                        'fps_max_menu 0\n'
                        'cl_disablehtmlmotd "1"\n'
                        'cl_forcepreload "1"\n'
                        'mat_queue_mode "-1"\n'
                        'r_eyegloss "0"\n'
                        'r_eyemove "0"\n'
                        'r_eyeshift_x "0"r_eyeshift_y "0"r_eyeshift_z "0"\n'
                        'r_eyesize "0"\n'
                        'r_dynamic “0”\n'
                        'r_drawparticles “0”\n'
                        'r_drawtracers_firstperson "0"\n'
                        'mat_powersavingsmode "0"\n'
                        'mat_queue_report "0"\n'
                        'gameinstructor_enable "0"\n'
                        'cl_autohelp "0"\n'
                        'cl_clearhinthistory "1"\n'
                        'muzzleflash_light "0"\n'
                        'cl_detail_avoid_force "0"\n'
                        'cl_debugrumble "0"\n'
                        'cl_join_advertise "2"\n'
                        'joystick_force_disabled "1"\n'
                        'joystick_force_disabled_set_from_options "1"\n'
                        'clear_anim_cache\n'
                        'clear_debug_overlays\n'
                        'r_flushlod\n'
                        'r_lightstyle "-1"\n'
                        'r_radiosity "4"\n'
                        'r_skin "0"\n'
                        'r_updaterefracttexture "0"\n'
                        'r_ambientfraction "0.1"\n'
                        'r_avglight "1"\n'
                        'r_avglightmap "0"\n'
                        'mat_loadtextures "1"\n'
                        'mat_norendering "0"\n'
                        'mat_show_texture_memory_usage "0"\n'
                        'mat_softwareskin "0"\n'
                        'mat_setvideomode 800 600 0'
                    )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi criada com sucesso !\n :)')
            elif varchk.get() == 9:
                with open(fr'C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\boost.cfg', 'w+') as file:
                    file.write(
                        'fps_max 0\n'
                        'fps_max_menu 0\n'
                        'cl_disablehtmlmotd "1"\n'
                        'cl_forcepreload "1"\n'
                        'mat_queue_mode "-1"\n'
                        'r_eyegloss "0"\n'
                        'r_eyemove "0"\n'
                        'r_eyeshift_x "0"r_eyeshift_y "0"r_eyeshift_z "0"\n'
                        'r_eyesize "0"\n'
                        'r_dynamic “0”\n'
                        'r_drawtracers_firstperson "0"\n'
                        'mat_powersavingsmode "0"\n'
                        'mat_queue_report "0"\n'
                        'gameinstructor_enable "0"\n'
                        'cl_clearhinthistory "1"\n'
                        'muzzleflash_light "0"\n'
                        'cl_detail_avoid_force "0"\n'
                        'cl_debugrumble "0"\n'
                        'cl_join_advertise "2"\n'
                        'joystick_force_disabled "1"\n'
                        'joystick_force_disabled_set_from_options "1"\n'
                        'clear_anim_cache\n'
                        'clear_debug_overlays\n'
                        'r_flushlod\n'
                        'r_lightstyle "-1"\n'
                        'r_radiosity "4"\n'
                        'r_skin "0"\n'
                        'r_updaterefracttexture "0"\n'
                        'r_ambientfraction "0.1"\n'
                        'r_avglight "1"\n'
                        'r_avglightmap "0"\n'
                        'mat_loadtextures "1"\n'
                        'mat_show_texture_memory_usage "0"\n'
                        'mat_softwareskin "0"\n'
                        'mat_setvideomode 1024 768 0'
                    )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi criada com sucesso !\n :)')
        except:
            tk.messagebox.showerror('Erro', 'Não foi possível modificar sua configuração, o jogo ou a configuração não foi encontrado(a) no sistema !\n :(')

    def btnRobloxAction():
        try:
            directory = str(dlg.askdirectory(title='Selecione a pasta de nome aleatório no diretório já aberto:', initialdir=(f'C:\\Users\\{user}\\AppData\\Local\\Roblox\\Versions')))
            origin = str(f'{directory}/PlatformContent/pc/textures')
            destiny = str(f'{directory}/PlatformContent/pc/TexturesBackup')
            def createbackup():
                shutil.copytree(origin, destiny)
            if os.path.exists(destiny):
                shutil.rmtree(destiny)
                createbackup()
            elif not os.path.exists(destiny):
                createbackup()
            shutil.rmtree(origin)
            os.mkdir(origin)
            shutil.copyfile(f'{destiny}/brdfLUT.dds', origin + '/brdfLUT.dds')
            shutil.copyfile(f'{destiny}/studs.dds', origin + '/studs.dds')
            shutil.copyfile(f'{destiny}/wangIndex.dds', origin + '/wangIndex.dds')
            if varchk.get() == 10:
                with open(fr'C:\Users\{user}\AppData\Local\Roblox\GlobalBasicSettings_13.xml', 'w+') as file:
                    file.write(
                                '<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">\n'
                                '	<External>null</External>\n'
                                '	<External>nil</External>\n'
                                '	<Item class="UserGameSettings" referent="RBX384B89760FC34E71AB9314917E2552FA">\n'
                                '		<Properties>\n'
                                '			<bool name="AllTutorialsDisabled">false</bool>\n'
                                '			<BinaryString name="AttributesSerialize"></BinaryString>\n'
                                '			<token name="CameraMode">0</token>\n'
                                '			<bool name="CameraYInverted">false</bool>\n'
                                '			<bool name="ChatVisible">true</bool>\n'
                                '			<string name="CompletedTutorials"></string>\n'
                                '			<bool name="ComputerCameraMovementChanged">false</bool>\n'
                                '			<token name="ComputerCameraMovementMode">0</token>\n'
                                '			<bool name="ComputerMovementChanged">true</bool>\n'
                                '			<token name="ComputerMovementMode">0</token>\n'
                                '			<token name="ControlMode">0</token>\n'
                                '			<string name="DefaultCameraID"></string>\n'
                                '			<bool name="Fullscreen">false</bool>\n'
                                '			<float name="GamepadCameraSensitivity">1</float>\n'
                                '			<int name="GraphicsQualityLevel"></int>\n'
                                '			<bool name="HasEverUsedVR">false</bool>\n'
                                '			<float name="MasterVolume">1</float>\n'
                                '			<bool name="MicroProfilerWebServerEnabled">false</bool>\n'
                                '			<float name="MouseSensitivity">1</float>\n'
                                '			<Vector2 name="MouseSensitivityFirstPerson">\n'
                                '				<X>1</X>\n'
                                '				<Y>1</Y>\n'
                                '			</Vector2>\n'
                                '			<Vector2 name="MouseSensitivityThirdPerson">\n'
                                '				<X>1</X>\n'
                                '				<Y>1</Y>\n'
                                '			</Vector2>\n'
                                '			<string name="Name">GameSettings</string>\n'
                                '			<bool name="OnScreenProfilerEnabled">false</bool>\n'
                                '			<bool name="PerformanceStatsVisible">false</bool>\n'
                                '			<int name="RCCProfilerRecordFrameRate">1</int>\n'
                                '			<int name="RCCProfilerRecordTimeFrame">1</int>\n'
                                '			<token name="SavedQualityLevel">1</token>\n'
                                '			<int64 name="SourceAssetId">-1</int64>\n'
                                '			<bool name="StartMaximized">false</bool>\n'
                                '			<Vector2 name="StartScreenPosition">\n'
                                '				<X>0</X>\n'
                                '				<Y>0</Y>\n'
                                '			</Vector2>\n'
                                '			<Vector2 name="StartScreenSize">\n'
                                '				<X>800</X>\n'
                                '				<Y>600</Y>\n'
                                '			</Vector2>\n'
                                '			<BinaryString name="Tags"></BinaryString>\n'
                                '			<bool name="TouchCameraMovementChanged">false</bool>\n'
                                '			<token name="TouchCameraMovementMode">0</token>\n'
                                '			<bool name="TouchMovementChanged">false</bool>\n'
                                '			<token name="TouchMovementMode">0</token>\n'
                                '			<bool name="UsedCoreGuiIsVisibleToggle">false</bool>\n'
                                '			<bool name="UsedCustomGuiIsVisibleToggle">false</bool>\n'
                                '			<bool name="UsedHideHudShortcut">false</bool>\n'
                                '			<bool name="VREnabled">true</bool>\n'
                                '			<int name="VRRotationIntensity">1</int>\n'
                                '			<bool name="VignetteEnabled">true</bool>\n'
                                '			<string name="gaID"></string>\n'
                                '		</Properties>\n'
                                '	</Item>\n'
                                '</roblox>'
                    )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi modificada com sucesso !\n :)')
            if varchk.get() == 11:
                with open(fr'C:\Users\{user}\AppData\Local\Roblox\GlobalBasicSettings_13.xml', 'w+') as file:
                    file.write(
                                '<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">\n'
                                '	<External>null</External>\n'
                                '	<External>nil</External>\n'
                                '	<Item class="UserGameSettings" referent="RBX384B89760FC34E71AB9314917E2552FA">\n'
                                '		<Properties>\n'
                                '			<bool name="AllTutorialsDisabled">false</bool>\n'
                                '			<BinaryString name="AttributesSerialize"></BinaryString>\n'
                                '			<token name="CameraMode">0</token>\n'
                                '			<bool name="CameraYInverted">false</bool>\n'
                                '			<bool name="ChatVisible">true</bool>\n'
                                '			<string name="CompletedTutorials"></string>\n'
                                '			<bool name="ComputerCameraMovementChanged">false</bool>\n'
                                '			<token name="ComputerCameraMovementMode">0</token>\n'
                                '			<bool name="ComputerMovementChanged">true</bool>\n'
                                '			<token name="ComputerMovementMode">0</token>\n'
                                '			<token name="ControlMode">0</token>\n'
                                '			<string name="DefaultCameraID"></string>\n'
                                '			<bool name="Fullscreen">false</bool>\n'
                                '			<float name="GamepadCameraSensitivity">1</float>\n'
                                '			<int name="GraphicsQualityLevel"></int>\n'
                                '			<bool name="HasEverUsedVR">false</bool>\n'
                                '			<float name="MasterVolume">1</float>\n'
                                '			<bool name="MicroProfilerWebServerEnabled">false</bool>\n'
                                '			<float name="MouseSensitivity">1</float>\n'
                                '			<Vector2 name="MouseSensitivityFirstPerson">\n'
                                '				<X>1</X>\n'
                                '				<Y>1</Y>\n'
                                '			</Vector2>\n'
                                '			<Vector2 name="MouseSensitivityThirdPerson">\n'
                                '				<X>1</X>\n'
                                '				<Y>1</Y>\n'
                                '			</Vector2>\n'
                                '			<string name="Name">GameSettings</string>\n'
                                '			<bool name="OnScreenProfilerEnabled">false</bool>\n'
                                '			<bool name="PerformanceStatsVisible">false</bool>\n'
                                '			<int name="RCCProfilerRecordFrameRate">1</int>\n'
                                '			<int name="RCCProfilerRecordTimeFrame">1</int>\n'
                                '			<token name="SavedQualityLevel">3</token>\n'
                                '			<int64 name="SourceAssetId">-1</int64>\n'
                                '			<bool name="StartMaximized">false</bool>\n'
                                '			<Vector2 name="StartScreenPosition">\n'
                                '				<X>0</X>\n'
                                '				<Y>0</Y>\n'
                                '			</Vector2>\n'
                                '			<Vector2 name="StartScreenSize">\n'
                                '				<X>800</X>\n'
                                '				<Y>600</Y>\n'
                                '			</Vector2>\n'
                                '			<BinaryString name="Tags"></BinaryString>\n'
                                '			<bool name="TouchCameraMovementChanged">false</bool>\n'
                                '			<token name="TouchCameraMovementMode">0</token>\n'
                                '			<bool name="TouchMovementChanged">false</bool>\n'
                                '			<token name="TouchMovementMode">0</token>\n'
                                '			<bool name="UsedCoreGuiIsVisibleToggle">false</bool>\n'
                                '			<bool name="UsedCustomGuiIsVisibleToggle">false</bool>\n'
                                '			<bool name="UsedHideHudShortcut">false</bool>\n'
                                '			<bool name="VREnabled">true</bool>\n'
                                '			<int name="VRRotationIntensity">1</int>\n'
                                '			<bool name="VignetteEnabled">true</bool>\n'
                                '			<string name="gaID"></string>\n'
                                '		</Properties>\n'
                                '	</Item>\n'
                                '</roblox>'
                    )
                tk.messagebox.showinfo('Operação Concluída', 'Sua Configuração foi modificada com sucesso !\n :)')
        except:
            tk.messagebox.showerror('Erro', 'Não foi possível completar a ação !\n :(')

    NewWindow = Toplevel()

    #Propriedades da janela
    NewWindow.title("Configurações")
    NewWindow.iconbitmap("files\icon.ico", )
    NewWindow.geometry("900x677")
    center(NewWindow)
    NewWindow.resizable(False, False)

    frame = ttk.Frame(NewWindow)
    bg = PhotoImage(file="files//Bg2.png")
    background_label=Label(frame, image=bg)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)

    btnFortnite = ttk.Button(frame, 
    text=(emoji.emojize(":engrenagem:Modificar Configuração", language="pt")),
    width=22,
    command=btnFortniteAction)

    btnGTAV = ttk.Button(frame, 
    text=(emoji.emojize(":engrenagem:Modificar Configuração", language="pt")),
    width=22,
    command=btnGTAVAction)

    btnWarzone = ttk.Button(frame,
    text=(emoji.emojize(":engrenagem:Modificar Configuração", language="pt")),
    width=22,
    command=btnWarzoneAction)

    btnValorant = ttk.Button(frame,
    text=(emoji.emojize(":engrenagem:Modificar Configuração", language="pt")),
    width=22,
    command=btnValorantAction)

    chk1 = ttk.Radiobutton(frame,
    text="Pc Fraco",
    value=0,
    variable=varchk)

    chk2 = ttk.Radiobutton(frame,
    text="Pc Forte",
    value=1,
    variable=varchk)

    chk3 = ttk.Radiobutton(frame,
    text="Pc Fraco",
    value=2,
    variable=varchk)

    chk4 = ttk.Radiobutton(frame,
    text="Pc Forte",
    value=3,
    variable=varchk)

    chk5 = ttk.Radiobutton(frame,
    text="Pc Fraco",
    value=4,
    variable=varchk)

    chk6 = ttk.Radiobutton(frame,
    text="Pc Forte",
    value=5,
    variable=varchk)

    chk7 = ttk.Radiobutton(frame,
    text="Pc Fraco",
    value=6,
    variable=varchk)

    chk8 = ttk.Radiobutton(frame,
    text="Pc Forte",
    value=7,
    variable=varchk)

    chk1.place(x=210, y=160)
    chk2.place(x=211, y=190)
    btnFortnite.place(x=165, y=225)
    chk3.place(x=615, y=240)
    chk4.place(x=616, y=270)
    btnGTAV.place(x=570, y=305)
    chk5.place(x=210, y=515)
    chk6.place(x=211, y=545)
    btnWarzone.place(x=165, y=580)
    chk7.place(x=610, y=515)
    chk8.place(x=611, y=545)
    btnValorant.place(x=565, y=580)
    
    frame.place(x=0, y=0, width=900, height=677)

    frame1 = ttk.Frame(NewWindow)
    bg1 = PhotoImage(file = "files//Bg3.png")
    background_label=Label(frame1, image=bg1)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)

    chk9 = ttk.Radiobutton(frame1,
    text="Pc Fraco",
    value=8,
    variable=varchk)

    chk10 = ttk.Radiobutton(frame1,
    text="Pc Forte",
    value=9,
    variable=varchk)

    chk11 = ttk.Radiobutton(frame1,
    text="Pc Fraco",
    value=10,
    variable=varchk)

    chk12 = ttk.Radiobutton(frame1,
    text="Pc Forte",
    value=11,
    variable=varchk)

    btnCSGO = ttk.Button(frame1,
    text=(emoji.emojize(":engrenagem:Modificar Configuração", language="pt")),
    width=22,
    command=btnCSGOAction)

    btnRoblox = ttk.Button(frame1,
    text=(emoji.emojize(":engrenagem:Modificar Configuração", language="pt")),
    width=22,
    command=btnRobloxAction)

    chk9.place(x=210, y=220)
    chk10.place(x=211, y=250)
    btnCSGO.place(x=165, y=285)
    chk11.place(x=610, y=230)
    chk12.place(x=611, y=260)
    btnRoblox.place(x=565, y=295)
    
    def btnSeta1Action():
        global varWin
        if varWin == 1:
            frame1.place_forget()
            frame.place(x=0, y=0, width=900, height=677)
            varWin = 0
        elif varWin == 0:
            frame.place_forget()
            frame1.place(x=0, y=0, width=900, height=677)
            varWin = 1
        else:
            frame.place_forget()
            frame1.place(x=0, y=0, width=900, height=677)
            varWin = 1
    
    def btnSeta2Action():
        global varWin
        if varWin == 0:
            frame.place_forget()
            frame1.place(x=0, y=0, width=900, height=677)
            varWin = 1
        elif varWin == 1:
            frame1.place_forget()
            frame.place(x=0, y=0, width=900, height=677)
            varWin = 0
        else:
            frame.place_forget()
            frame1.place(x=0, y=0, width=900, height=677)
            varWin = 1

    imgButton1 = PhotoImage(file=".\\files\\button.png")
    imgButton2 = PhotoImage(file=".\\files\\button1.png")

    btnSeta1 = Button(NewWindow,
    image=imgButton2,
    border=False,
    relief=GROOVE,
    bd=0,
    bg="#994cf1",
    command=btnSeta1Action)

    btnSeta2 = Button(NewWindow,
    image=imgButton1,
    border=False,
    relief=GROOVE,
    bd=0,
    bg="#994cf1",
    command=btnSeta2Action)

    btnSeta2.place(x=390, y=625)
    btnSeta1.place(x=465, y=625)

    NewWindow.mainloop()

app = ThemedTk(theme="breeze")

app.geometry("627x389")
app.resizable(False, False)
center(app)

app.title("KOCKIE OPTIMIZER V0.7")

app.iconbitmap("files\icon.ico")

try:
    image=ImageTk.PhotoImage(Image.open("files\\Bg.png"))
    background_label=Label(app,image=image)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
except:
    app['background']='#454545'

#Botões
btn1 = ttk.Button(app, 
text="Otimizar Windows",
width=20,
command=btn1Action)

btn2 = ttk.Button(app, 
text="Configurações de Jogos",
width=21,
command=btn2Action)

btn3 = ttk.Button(app,
text="Desinstalar apps inúteis",
command=btn3Action)

btn4 = ttk.Button(app,
text="Instalar Apps/Drivers Úteis",
command=btn4Action)

photo = PhotoImage(file = r"files\YT.png") 
photoimage = photo.subsample(3,3)
btn5 = ttk.Button(app,
image=photo,
compound=LEFT,
text="YouTube",
command=btn5Action)

photo2 = PhotoImage(file = r"files\DS.png") 
photoimage2 = photo.subsample(3,3)
btn6 = ttk.Button(app,
image=photo2,
compound=LEFT,
text="Discord",
command=btn6Action)

btn1.place(x=147, y=158)
btn2.place(x=144, y=195)
btn3.place(x=324, y=195)
btn4.place(x=318, y=158)
btn5.place(x=507, y=330, width=100, height=40)
btn6.place(x=400, y=330, width=100, height=40)

tk.messagebox.showinfo('Aviso', 'Lembre-se de criar um ponto de restauração antes de fazer mudanças grandes no windows !')

app.mainloop()
