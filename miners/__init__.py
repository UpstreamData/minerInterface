import asyncssh
import logging
import ipaddress

from data import MinerData


class BaseMiner:
    def __init__(self, *args) -> None:
        self.ip = None
        self.uname = "root"
        self.pwd = "admin"
        self.api = None
        self.api_type = None
        self.model = None
        self.light = None
        self.hostname = None
        self.nominal_chips = 1
        self.version = None
        self.fan_count = 2

    def __repr__(self):
        return f"{'' if not self.api_type else self.api_type} {'' if not self.model else self.model}: {str(self.ip)}"

    def __lt__(self, other):
        return ipaddress.ip_address(self.ip) < ipaddress.ip_address(other.ip)

    def __gt__(self, other):
        return ipaddress.ip_address(self.ip) > ipaddress.ip_address(other.ip)

    def __eq__(self, other):
        return ipaddress.ip_address(self.ip) == ipaddress.ip_address(other.ip)

    async def _get_ssh_connection(self) -> asyncssh.connect:
        """Create a new asyncssh connection"""
        try:
            conn = await asyncssh.connect(
                str(self.ip),
                known_hosts=None,
                username=self.uname,
                password=self.pwd,
                server_host_key_algs=["ssh-rsa"],
            )
            return conn
        except asyncssh.misc.PermissionDenied:
            try:
                conn = await asyncssh.connect(
                    str(self.ip),
                    known_hosts=None,
                    username="root",
                    password="admin",
                    server_host_key_algs=["ssh-rsa"],
                )
                return conn
            except Exception as e:
                # logging.warning(f"{self} raised an exception: {e}")
                raise e
        except OSError as e:
            logging.warning(f"Connection refused: {self}")
            raise e
        except Exception as e:
            # logging.warning(f"{self} raised an exception: {e}")
            raise e

    async def fault_light_on(self) -> bool:
        return False

    async def fault_light_off(self) -> bool:
        return False

    async def send_file(self, src, dest):
        async with (await self._get_ssh_connection()) as conn:
            await asyncssh.scp(src, (conn, dest))

    async def check_light(self):
        return self.light

    async def get_board_info(self):
        return None

    async def get_config(self):
        return None

    async def get_hostname(self):
        return None

    async def get_model(self):
        return None

    async def reboot(self):
        return False

    async def restart_backend(self):
        return False

    async def send_config(self, *args, **kwargs):
        return None

    async def get_mac(self):
        return None

    async def get_data(self):
        return MinerData(ip=str(self.ip))
