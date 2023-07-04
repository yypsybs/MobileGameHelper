from module.alas import AzurLaneAutoScript


class AlasImplement(AzurLaneAutoScript):
    def restart(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_restart()

    def start(self):
        from tasks.login.login import Login
        Login(self.config, device=self.device).app_start()

    def goto_main(self):
        pass


if __name__ == '__main__':
    src = AlasImplement('alas')
    src.loop()
