import tarfile

def read_tarfile(target_file):
    # 압축 방법 : gz, bz2, xz
    with tarfile.open(target_file, "r") as tar:
        # print(tar.getnames())
        # file_info = tar.getmember("descriptions/._description01.txt")
        #print(file_info.name, file_info.size, file_info.mode)
        # 420의 의미 : rwx rwx rwx : r-- -w- --- 
        for member in tar.getmembers():
            print(member.name, member.size, member.mode)

def read_file_in_tar(target_file, member_file):
    with tarfile.open(target_file, "r") as tar:
        with tar.extractfile(member_file) as file:
            print(file.read())

if __name__ == "__main__":
    # read_tarfile("archive.tar.gz")
    read_file_in_tar("archive.tar.gz", "descriptions/description01.txt")