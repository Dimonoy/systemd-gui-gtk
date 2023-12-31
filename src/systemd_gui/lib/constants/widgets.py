"""Defines usable widgets names assigned in the .glade files.
"""


WIDGETS = {'app_win': 'ApplicationWindow',
           'menubar': 'MenuBar',
           'toolbar': 'ActionBar',
           'stack': 'Stack',
           'about': 'AboutDialog',

           'btn': {'apply': 'ApplyButton',
                   'reset': 'ResetButton',
                   'start': 'StartButton',
                   'stop': 'StopButton',
                   'restart': 'RestartButton',
                   'reload': 'ReloadButton',
                   'enable': 'EnableButton',
                   'disable': 'DisableButton',
                   'mask': 'MaskButton',
                   'unmask': 'UnmaskButton'},
           'menu': {'file': {'apply': 'ApplyMenuItem',
                             'reset': 'ResetMenuItem',
                             'start': 'StartMenuItem',
                             'stop': 'StopMenuItem',
                             'restart': 'RestartMenuItem',
                             'reload': 'ReloadMenuItem',
                             'enable': 'EnableMenuItem',
                             'disable': 'DisableMenuItem',
                             'mask': 'MaskMenuItem',
                             'unmask': 'UnmaskMenuItem',
                             'manpage': 'ManPageMenuItem',
                             'quit': 'QuitMenuItem'},
                    'view': {'refresh': 'RefreshMenuItem',
                             'toolbar_chk': 'ToolbarCheckMenuItem',
                             'load_state_chk': 'LoadStateCheckMenuItem',
                             'active_state_chk': 'ActiveStateCheckMenuItem',
                             'sub_state_chk': 'SubStateCheckMenuItem',
                             'desc_chk': 'DescriptionCheckMenuItem'},
                    'options': {},
                    'help': {'about': 'AboutMenuItem'}},

           'units': {'search': 'UnitsSearchEntry',
                     'user_chk': 'UserCheckButton',
                     'unloaded_chk': 'UnloadedCheckButton',
                     'inactive_chk': 'InactiveCheckButton',
                     'masked_chk': 'MaskedCheckButton',
                     'types': 'UnitsTypeComboBox',
                     'table': 'UnitsTreeView',
                     'selection': 'UnitsTreeSelection',
                     'total': 'UnitsTotalLabel',
                     'status': 'UnitsStatusLabel'},

           'load_state_col': 'LoadStateColumn',
           'active_state_col': 'ActiveStateColumn',
           'sub_state_col': 'SubStateColumn',
           'desc_col': 'DescriptionColumn',

           'configs': {'search': 'ConfigsSearchEntry',
                       'table': 'ConfigsTreeView',
                       'selection': 'ConfigsTreeSelection',
                       'total': 'ConfigsTotalLabel',
                       'status': 'ConfigsStatusLabel'},

           'timers': {'table': 'TimersTreeView',
                      'selection': 'TimersTreeSelection',
                      'total': 'TimersTotalLabel',
                      'status': 'TimersStatusLabel'},

           'store': {'units': 'UnitsListStore',
                     'configs': 'ConfigsListStore',
                     'timers': 'TimersListStore'}}
