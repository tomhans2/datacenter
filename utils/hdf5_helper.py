import h5py

def write_to_h5():
    pass

if __name__ == '__main__':
    with h5py.File("mytestfile.hdf5", "w") as f:
        dset = f.create_dataset("mydataset", (100,), dtype='i')