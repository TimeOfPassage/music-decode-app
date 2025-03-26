from utils.command_utils import CommandUtils


class NCMHelper:

    # 静态方法，用于启动ncm
    @staticmethod
    def start(source_file: str, target_file: str, execute_path: str = "./um"):
        ret_code = CommandUtils.run(f"{execute_path} -i {source_file} -o {target_file}", shell=True)
        # 如果返回值不为0，则抛出异常
        if ret_code != 0:
            raise Exception("Failed to start ncm")


if __name__ == '__main__':
    NCMHelper.start("/Users/charles.h/Desktop/艾辰-错位时空.ncm", "/Users/charles.h/Desktop/1.mp3", "/Users/charles.h/Documents/project-info/music-decode-app/um")
