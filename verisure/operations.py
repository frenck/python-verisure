NO_HELP_YET = "No help written yet"

class VariableTypes: 
    DeviceLabel = 0
    SmartPlugState = 1


OPERATIONS = {
    "fetch_all_installations": {
        "name": "fetchAllInstallations",
        "query": "query fetchAllInstallations($email: String!) {\n  account(email: $email) {\n    installations {\n      giid\n      alias\n      customerType\n      dealerId\n      subsidiary\n      pinCodeLength\n      locale\n      address {\n        street\n        city\n        postalNumber\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"email": None},
        "help": "Fetch installations",
    },
    "guardian_sos": {
        "name": "GuardianSos",
        "query": "query GuardianSos {\n  guardianSos {\n    serverTime\n    sos {\n      fullName\n      phone\n      deviceId\n      deviceName\n      giid\n      type\n      username\n      expireDate\n      warnBeforeExpireDate\n      contactId\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {},
        "help": NO_HELP_YET,
    },
    "is_guardian_activated": {
        "name": "IsGuardianActivated",
        "query": "query IsGuardianActivated($giid: String!, $featureName: String!) {\n  installation(giid: $giid) {\n    activatedFeature {\n      isFeatureActivated(featureName: $featureName)\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None, "featureName": "GUARDIAN"},
        "help": NO_HELP_YET,
    },
    "smart_plugs": {
        "name": "SmartPlug",
        "query": "query SmartPlug($giid: String!) {\n  installation(giid: $giid) {\n    smartplugs {\n      device {\n        deviceLabel\n        area\n        __typename\n      }\n      currentState\n      icon\n      isHazardous\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": "Read status of all smart plugs",
    },
    "smart_plug": {
        "name": "SmartPlug",
        "query": "query SmartPlug($giid: String!, $deviceLabel: String!) {\n  installation(giid: $giid) {\n    smartplugs(filter: {deviceLabels: [$deviceLabel]}) {\n      device {\n        deviceLabel\n        area\n        __typename\n      }\n      currentState\n      icon\n      isHazardous\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {"deviceLabel": VariableTypes.DeviceLabel},
        "session_variables": {"giid": None},
        "help": "Read status of a single smart plug",
    },
    "door_window": {
        "name": "DoorWindow",
        "query": "query DoorWindow($giid: String!) {\n  installation(giid: $giid) {\n    doorWindows {\n      device {\n        deviceLabel\n        __typename\n      }\n      type\n      area\n      state\n      wired\n      reportTime\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": "Read status of door and window sensors",
    },
    "remaining_sms": {
        "name": "RemainingSms",
        "query": "query RemainingSms($giid: String!) {\n  installation(giid: $giid) {\n    remainingSms\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": "Get remaing number of SMS",
    },
    "charge_sms": {
        "name": "ChargeSms",
        "query": "query ChargeSms($giid: String!) {\n  installation(giid: $giid) {\n    chargeSms {\n      chargeSmartPlugOnOff\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "climate": {
        "name": "Climate",
        "query": "query Climate($giid: String!) {\n  installation(giid: $giid) {\n    climates {\n      device {\n        deviceLabel\n        area\n        gui {\n          label\n          __typename\n        }\n        __typename\n      }\n      humidityEnabled\n      humidityTimestamp\n      humidityValue\n      temperatureTimestamp\n      temperatureValue\n      thresholds {\n        aboveMaxAlert\n        belowMinAlert\n        sensorType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "arm_state": {
        "name": "ArmState",
        "query": "query ArmState($giid: String!) {\n  installation(giid: $giid) {\n    armState {\n      type\n      statusType\n      date\n      name\n      changedVia\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "smart_button": {
        "name": "SmartButton",
        "query": "query SmartButton($giid: String!) {\n  installation(giid: $giid) {\n    smartButton {\n      entries {\n        smartButtonId\n        icon\n        label\n        color\n        active\n        action {\n          actionType\n          expectedState\n          target {\n            ... on Installation {\n              alias\n              __typename\n            }\n            ... on Device {\n              deviceLabel\n              area\n              gui {\n                label\n                __typename\n              }\n              featureStatuses(type: \"SmartPlug\") {\n                device {\n                  deviceLabel\n                  __typename\n                }\n                ... on SmartPlug {\n                  icon\n                  isHazardous\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "broadband": {
        "name": "Broadband",
        "query": "query Broadband($giid: String!) {\n  installation(giid: $giid) {\n    broadband {\n      testDate\n      isBroadbandConnected\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "capability": {
        "name": "Capability",
        "query": "query Capability($giid: String!) {\n  installation(giid: $giid) {\n    capability {\n      current\n      gained {\n        capability\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "user_trackings": {
        "name": "userTrackings",
        "query": "query userTrackings($giid: String!) {\n  installation(giid: $giid) {\n    userTrackings {\n      isCallingUser\n      webAccount\n      status\n      xbnContactId\n      currentLocationName\n      deviceId\n      name\n      initials\n      currentLocationTimestamp\n      deviceName\n      currentLocationId\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "user_tracking_installation_config": {
        "name": "userTrackingInstallationConfig",
        "query": "query userTrackings($giid: String!) {\n  installation(giid: $giid) {\n    userTrackings {\n      isCallingUser\n      webAccount\n      status\n      xbnContactId\n      currentLocationName\n      deviceId\n      name\n      initials\n      currentLocationTimestamp\n      deviceName\n      currentLocationId\n      __typename\n    }\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
    "permissions": {
        "name": "Permissions",
        "query": "query Permissions($giid: String!, $email: String!) {\n  permissions(giid: $giid, email: $email) {\n    accountPermissionsHash\n    name\n    __typename\n  }\n}\n",
        "variables": {},
        "session_variables": {"giid": None, "email": None},
        "help": NO_HELP_YET,
    },
    "update_state": {
        "name": "UpdateState",
        "query": "mutation UpdateState($giid: String!, $deviceLabel: String!, $state: Boolean!) {\n  SmartPlugSetState(giid: $giid, input: [{deviceLabel: $deviceLabel, state: $state}])\n}\n",
        "variables": {"deviceLabel": VariableTypes.DeviceLabel, "state": VariableTypes.SmartPlugState},
        "session_variables": {"giid": None},
        "help": NO_HELP_YET,
    },
}