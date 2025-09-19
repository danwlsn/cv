from datetime import datetime
import os

from fabric import task
from fabric.connection import Connection

@task
def deploy_api(con: Connection):
    # setup vars
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    zip_name = "app.tar.gz"

    # Local dirs
    DIR = os.path.dirname(__file__)
    local_zip = os.path.join(DIR, zip_name)

    # Remote dirs
    app_dir = "/var/www/cv-api/"
    deploy_dir = os.path.join(app_dir, now)
    zip_path = os.path.join(app_dir, zip_name)
    latest_path = os.path.join(app_dir, "latest")

    # prepare the build
    con.local("make api-build")
    con.put(local_zip, app_dir)

    print("Removing latest")
    con.run(f"rm {latest_path}", warn=True)
    with con.cd(app_dir):
        # keep only the latest 5 versions
        con.run("ls -1td -- */ | head -n -5 | xargs rm -r", warn=True)

    # xtract the build
    print("deploying zip")
    con.run(f"mkdir -p {deploy_dir}")
    con.run(f"tar -xzf {zip_path} -C {deploy_dir} --strip-components=1")
    con.run(f"ln -s {deploy_dir} {latest_path}")
    with con.cd(latest_path):
        con.run("python3.13 -m venv venv")
        con.run("source venv/bin/activate && pip install -r requirements.txt")

    con.sudo("systemctl restart cv-api", pty=True)

    # clean up
    print("clean up")
    con.local(f"rm {local_zip}")
    con.run(f"rm {zip_path}")
