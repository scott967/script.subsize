#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2025 Scott Smart
# This program is Free Software see LICENSE file for details
# pylint: disable=consider-using-f-string
#
#
"""Launches a select dialog that allows the user to select one of the defined
Kodi subtitle font sizes, for text subs without styles (eg, ASS)  The user
selection is saved as a Kodi player/video/subtitles fontsize setting
"""

import json

import xbmc
import xbmcaddon
import xbmcgui

LOG_LEVEL = [xbmc.LOGDEBUG, xbmc.LOGWARNING, xbmc.LOGINFO]
JSON_GET_SUBSIZE = {"jsonrpc":"2.0","id": 1,
                    "method":"Settings.GetSettingValue", 
                    "params": {"setting": "subtitles.fontsize"} }
JSON_SET_SUBSIZE = {"jsonrpc":"2.0","id": 1,
                    "method":"Settings.SetSettingValue", 
                    "params": {"setting": "subtitles.fontsize", "value":12} }
FONT_SIZE = [str(12 + (2*i)) for i in range(32)]
addon= xbmcaddon.Addon()
ADDON_ID = addon.getAddonInfo('id')
DIALOG_HEADING = xbmc.getLocalizedString(36186)

class Main:
    """All processing happens in the class
    """
    def log(self, msg: str, level: int=LOG_LEVEL[0]) -> None:
        """wraps Kodi log function

        Args:
            msg (str): string to write to debug log
            level (str) either DEBUG, WARNING, or INFO
        """
        xbmc.log(f'{ADDON_ID}: {msg}', level)

    def get_current_size(self) ->int:
        """calls Kodi JSON-RPC to get the current value of setting subtitles.fontsize

        Returns:
            int: the current font size
        """
        response:dict = json.loads(xbmc.executeJSONRPC(json.dumps(JSON_GET_SUBSIZE)))
        #self.log(f'response {response}')
        if 'result' in response:
            #self.log(f'current size {response["result"].get("value", 0)}')
            return int(response['result'].get('value', 0))
        return 0

    def set_font_size(self, font_size:int) ->bool:
        """calls Kodi JSON-RPC to update setting subtitles.fontsize

        Args:
            font_size (int): the new subtitle font size

        Returns:
            bool: True if succeeded
        """
        json_set = JSON_SET_SUBSIZE
        json_set['params']['value'] = font_size
        #self.log(f'set_font_size json command is {json_set}')
        response:dict = json.loads(xbmc.executeJSONRPC(json.dumps(json_set)))
        #self.log(f'response {response}')
        if 'result' in response and response['result']:
            return True
        return False

    def __init__(self) -> None:
        """constructor runs the code to update the subtitle font size
        """
        #self.log(f'font size list {FONT_SIZE}')
        sub_size = self.get_current_size()
        self.log(f'current subtitle subsize is {sub_size}')
        sub_size = self.get_new_size(sub_size)
        result = self.set_font_size(sub_size)
        #self.log(f'result {result}')
        if result:
            self.log(f'Setting subtitle fontsize to {sub_size}')
        else:
            self.log('Unable to set new subtitles fontsize')

    def get_new_size(self, sub_size: int) -> int:
        """launches select dialog for user selection of font size

        Args:
            sub_size (int): the current font size

        Returns:
            int: the new user selected font size
        """
        new_size = 12 + (2*xbmcgui.Dialog().select(DIALOG_HEADING,
                        FONT_SIZE, preselect=((sub_size - 12)//2)))
        #self.log(f'newsize is {new_size}')
        return new_size if new_size > 10 else sub_size

if __name__ == "__main__":
    Main()
