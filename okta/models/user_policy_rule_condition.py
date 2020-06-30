"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class UserPolicyRuleCondition(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.exclude = config["exclude"]\
                if "exclude" in config else None
            self.inactivity = config["inactivity"]\
                if "inactivity" in config else None
            self.include = config["include"]\
                if "include" in config else None
            self.lifecycle_expiration = config["lifecycleExpiration"]\
                if "lifecycleExpiration" in config else None
            self.password_expiration = config["passwordExpiration"]\
                if "passwordExpiration" in config else None
            self.user_lifecycle_attribute = config["userLifecycleAttribute"]\
                if "userLifecycleAttribute" in config else None
        else:
            self.exclude = None
            self.inactivity = None
            self.include = None
            self.lifecycle_expiration = None
            self.password_expiration = None
            self.user_lifecycle_attribute = None

# End of File Generation
