class ResponseForDaysOff:
    @classmethod
    def build(cls):
        return [
            {
                "_id": "someId",
                "_approvalRule": {
                    "users": [],
                    "managerOfFirstApprover": [],
                    "company": [],
                    "office": [],
                    "area": [],
                    "department": [],
                    "team": []
                },
                "attachments": [],
                "_policyType": "Day",
                "_approvers": [],
                "_userId": "someUserId",
                "_policyId": "somePolicyId",
                "_partOfDayFrom": "StartOfDay",
                "_partOfDayTo": "EndOfDay",
                "_description": "",
                "_from": "2022-04-14T00:00:00.000Z",
                "_to": "2022-04-14T23:59:59.999Z",
                "_updatedById": "someOtherUserId",
                "ownerId": "someUserId",
                "_createdById": "someUserId",
                "_timeOffTypeId": "someTypeId",
                "_timeOffTypeName": "Vacaciones",
                "_workTime": False,
                "_countNaturalDays": False,
                "_policyName": "Vacaciones 23",
                "_type": "Request",
                "status": "Processed",
                "_duration": 1,
                "_workingDays": 1,
                "_splitRequests": [
                    {
                        "_id": "6257803c5d15b20ef311b208",
                        "_from": "2022-04-14T00:00:00.000Z",
                        "_to": "2022-04-14T23:59:59.999Z",
                        "_duration": 1,
                        "_workingDays": 1,
                        "_partOfDayFrom": "StartOfDay",
                        "_partOfDayTo": "EndOfDay"
                    }
                ],
                "_approvedBy": [
                    {
                        "_id": "someAdminUserId",
                        "_userId": "someOtherUserId",
                        "_approvedAt": "2022-03-24T10:58:06.050Z"
                    }
                ],
                "_oldSplitRequests": [],
                "_createdAt": "2022-03-23T16:59:12.340Z",
                "_updatedAt": "2022-04-14T02:00:28.635Z",
                "_processedWorkingDays": 1
            },
            {
                "_id": "someId",
                "_approvalRule": {
                    "users": [],
                    "managerOfFirstApprover": [],
                    "company": [],
                    "office": [],
                    "area": [],
                    "department": [],
                    "team": []
                },
                "attachments": [],
                "_policyType": "Day",
                "_approvers": [],
                "_userId": "someUserId",
                "_policyId": "somePolicyId",
                "_partOfDayFrom": "StartOfDay",
                "_partOfDayTo": "EndOfDay",
                "_description": "Vacaciones Julio",
                "_from": "2022-07-14T00:00:00.000Z",
                "_to": "2022-07-20T23:59:59.999Z",
                "_updatedById": "someUserId",
                "ownerId": "someUserId",
                "_createdById": "someUserId",
                "_timeOffTypeId": "someTypeId",
                "_timeOffTypeName": "Vacaciones",
                "_workTime": False,
                "_countNaturalDays": False,
                "_policyName": "Vacaciones 23",
                "_type": "Request",
                "status": "Cancelled",
                "_duration": 7,
                "_workingDays": 5,
                "_splitRequests": [
                    {
                        "_id": "6277eb477eddd61f4304b964",
                        "_from": "2022-07-14T00:00:00.000Z",
                        "_to": "2022-07-20T23:59:59.999Z",
                        "_duration": 7,
                        "_workingDays": 5,
                        "_partOfDayFrom": "StartOfDay",
                        "_partOfDayTo": "EndOfDay"
                    }
                ],
                "_approvedBy": [],
                "_oldSplitRequests": [],
                "_createdAt": "2022-05-08T16:09:44.046Z",
                "_updatedAt": "2022-05-12T14:48:14.705Z",
                "decision": "Colisionan con las vacaciones de Ángel"
            },
            {
                "_id": "someId",
                "_approvalRule": {
                    "users": [],
                    "managerOfFirstApprover": [],
                    "company": [],
                    "office": [],
                    "area": [],
                    "department": [],
                    "team": []
                },
                "attachments": [],
                "_policyType": "Day",
                "_approvers": [],
                "_userId": "someUserId",
                "_policyId": "somePolicyId",
                "_partOfDayFrom": "StartOfDay",
                "_partOfDayTo": "EndOfDay",
                "_description": "Vacaciones Julio v2",
                "_from": "2022-07-12T00:00:00.000Z",
                "_to": "2022-07-18T23:59:59.999Z",
                "_updatedById": "someUserId",
                "ownerId": "someUserId",
                "_createdById": "someUserId",
                "_timeOffTypeId": "someTypeId",
                "_timeOffTypeName": "Vacaciones",
                "_workTime": False,
                "_countNaturalDays": False,
                "_policyName": "Vacaciones 23",
                "_type": "Request",
                "status": "Pending",
                "_duration": 7,
                "_workingDays": 5,
                "_splitRequests": [
                    {
                        "_id": "627d1e6ce99a697580d54d3e",
                        "_from": "2022-07-12T00:00:00.000Z",
                        "_to": "2022-07-18T23:59:59.999Z",
                        "_duration": 7,
                        "_workingDays": 5,
                        "_partOfDayFrom": "StartOfDay",
                        "_partOfDayTo": "EndOfDay"
                    }
                ],
                "_approvedBy": [],
                "_oldSplitRequests": [],
                "_createdAt": "2022-05-12T14:49:16.467Z",
                "_updatedAt": "2022-05-12T14:49:16.467Z"
            }
        ]
