# Installation instructions
The following instructions are helpful in setting up a Eurotoken gateway
(and optionally Trustchain clients) entirely separated from the existing
networks and communities.

First, decide whether to execute this code directly on the host machine
or through Docker. Then follow *Gateway Changes*, either *Run With Docker*
or *Run Without Docker*, then *Trustchain Changes*.

## Gateway Changes
First we'll change the source code of the gateway slightly to ensure
an environment separated from the existing communities.

1. In `backend/stablecoin/blockchain/ipv8/eurotoken/community.py`,
change the `community_id` to something unique.
2. In `backend/stablecoin/run_coin.py`, change the values of
`GATEWAY_NAME`, `GATEWAY_HOSTNAME`, and `GATEWAY_IP`.
    1. Note that `0.0.0.0` is a perfectly valid IP and hostname.
3. Create the folders `backend/stablecoin/.ssh/eurotoken/trustchain`
and `backend/stablecoin/.ssh/eurotoken/tikkie`.
4. Obtain an ABN AMRO developer key for the Tikkie sandbox and
paste it in `backend/stablecoin/.ssh/eurotoken/tikkie` with
filename `abn_stablecoin_key` (no file extension).
5. Generate a Trustchain key and paste it in
`backend/stablecoin/.ssh/eurotoken/trustchain` with filename
`ec.pem`.
    1. An easy way of generating a Trustchain key is by
    executing `backend/stablecoin/generate_trustchain_key.py`.
    However, first modify the `filepath` variable to point to
    the correct path and filename.
6. Create the empty folder `frontend/dist`. 

## Run Without Docker
0. Install Python 3.7, Conda or Pip, npm, and Vue.js.
1. Use Conda or Pip to install `backend/requirements.txt`.
2. Install *libsodium* with help from [this link](https://github.com/Tribler/py-ipv8/blob/master/doc/preliminaries/install_libsodium.rst).
3. You can now start the backend with `backend/stablecoin/run_coin.py`
and the frontend by navigating to `frontend` and executing `npm run serve`.

## Run With Docker
0. Install Docker.
1. Execute `docker-compose up` from the root of the repository.
    - Append the `-d` parameter to execute the command in the background.
    - Execute `docker-compose stop` to stop the containers.
2. In another prompt, execute
`docker exec -it -u root stablecoin-exchange_app_1 sh`
to enter the terminal of the gateway backend container.
3. You can now start the backend with `python run_coin.py`.
4. In another window, enter the terminal of
the gateway frontend container using
`docker exec -it -u root stablecoin-exchange_proxy_1 sh`.
5. Install npm and Node.js there by executing
`apk add --update npm`.
6. Enter the frontend directory using `cd vol/frontend`.
7. Build the frontend from the source by executing
`npm run build`. This will create a `dist` folder in
this directory containing the static files of the webpage.
8. Copy the contents of `dist` to `vol/static` by executing
`cp -r dist/. ../static`.
9. Move one folder up to `vol` using `cd ../`.
10. Run `npm install -g serve`, then `serve -s static` or
see the [Vue.js documentation on deployment](https://cli.vuejs.org/guide/deployment.html#general-guidelines).
11. Connect to `localhost:8080` in an external browser.
You should now see the GUI of the Eurotoken gateway.
12. Optionally, install a text editor such as Nano using
`apk update`, then `apk add nano`, for editing files
in the containers directly.

## Trustchain Changes
Next, we'll change the source code of the [Trustchain Superapp](https://github.com/Tribler/trustchain-superapp).
1. In `common/build.grade`, change `DEFAULT_GATEWAY_IP` and `DEFAULT_GATEWAY_NAME`
to the values you set in the gateway. Also change `DEFAULT_GATEWAY_PK`.
If you are unsure what to put for `DEFAULT_GATEWAY_PK`, change the
debug level of `backend/stablecoin/run_coin.py` to `DEBUG`
instead of `INFO`, start `backend/stablecoin/run_coin.py` and look
for the message `The trustchain community started with Public Key: b'<key>'`.
2. In `eurotoken/…/EuroTokenCommunity.kt`, change `serviceId` to the same
value you gave `community_id` in `backend/stablecoin/blockchain/ipv8/eurotoken/community.py`.