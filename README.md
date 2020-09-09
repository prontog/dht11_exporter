# DHT11 exporter

Export DHT11 sensor metrics in *Prometheus* *node_exporter*'s **textfile** format.

## Dependencies

 * Prometheus (obviously)
 * Node Exporter with textfile collector
 * Python 3
 * Adafruit_DHT python module

## Install

- copy `dht11_exporter` to `/usr/local/bin`.
- copy `dht11_exporter.service` to `/etc/systemd/system`
- enable and start `dht11_exporter`

For example you can deploy using git:

``` bash
sudo pip3 install Adafruit_DHT
cd /opt
sudo git clone https://github.com/prontog/dht11_exporter
cd dht11_exporter
sudo ln -s /opt/dht11_exporter/dht11_exporter.service /etc/systemd/system
sudo ln -s /opt/dht11_exporter/dht11_exporter /usr/local/bin
sudo ln -s /opt/dht11_exporter/dht11.py /usr/local/bin
sudo systemctl enable dht11_exporter
sudo systemctl start dht11_exporter
```

## Configure your node exporter

Make sure your node exporter uses `textfile` in `--collectors.enabled` and add the following parameter: `--collector.textfile.directory=/var/lib/node_exporter`

## Example queries

```
dht11_temperature{job="node", device="DHT11"}
```
