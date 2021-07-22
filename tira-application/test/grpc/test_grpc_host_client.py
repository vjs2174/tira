import grpc
from google.protobuf.empty_pb2 import Empty
from time import sleep
import sys

sys.path.append('../../src/tira')
from proto import tira_host_pb2, tira_host_pb2_grpc


class TestGrpcHostClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50052')
        self.stub = tira_host_pb2_grpc.TiraApplicationServiceStub(self.channel)

    def __del__(self):
        self.channel.close()

    def set_state(self, vm_id, vm_state, slp=5):
        """ Wait for 10 seconds, then call the set_state method of the applications server,
         this means, we tell the application that the vm now changed it's state to vm_state """
        sleep(slp)
        print("after_sleep")
        response = self.stub.set_state(
            tira_host_pb2.SetVmState(status=tira_host_pb2.Status.SUCCESS, state=vm_state, vmId=vm_id))
        return response
