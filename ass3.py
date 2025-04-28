from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank=comm.rank
send_buf=np.array([])
if rank==0:
    arr= np.array([12,545,455,5765,56,46,636,25635,4656,4588,456,4569])
    arr.shape=(3,4)
    send_buf=arr.flatten()
recv_buf=np.empty(3,dtype=int)
send_buf=np.array_split(send_buf,comm.Get_size())
send_buf=comm.scatter(send_buf,root=0)
local_sum=np.sum(send_buf)
print("Local sum at rank{0}:{1}".format(rank,local_sum))
recv_buf=comm.reduce(local_sum,root=0)
if rank==0:
 print("Global sum:"+str(recv_buf))