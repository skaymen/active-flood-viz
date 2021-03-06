FROM debian:stretch
MAINTAINER James McFeeters "jmcfeeters@usgs.gov"
RUN apt-get update && apt-get install -y \
    python3-pip \
    nginx-light \
    curl \
    apt-transport-https \
    git

COPY . /app
WORKDIR /app

RUN cp DOIRootCA2.cer /etc/ssl/certs/DOIRootCA2.pem \
&& cat DOIRootCA2.cer >> /etc/ssl/certs/ca-certificates.crt

RUN rm -f /etc/apt/sources.list.d/chris-lea-node_js-jessie.list \
&& curl --cacert DOIRootCA2.cer https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
&& echo 'deb https://deb.nodesource.com/node_6.x jessie main' > /etc/apt/sources.list.d/nodesource.list \
&& apt-get update \
&& apt-get install -y nodejs

RUN pip3 --cert /app/DOIRootCA2.cer install -r requirements.txt

RUN npm config set cafile "/app/DOIRootCA2.cer" \
&& npm update

RUN node_modules/bower/bin/bower install --allow-root

EXPOSE 5050

ENTRYPOINT ["python3"]
CMD ["run.py" ,"--host", "0.0.0.0", "--freeze"]
