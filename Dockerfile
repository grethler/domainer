FROM python:3

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    libgconf-2-4 \
    libnss3 \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get install -y wget gnupg2 \
    && wget -q https://dl.google.com/linux/linux_signing_key.pub -O- | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable

# see https://github.com/SeleniumHQ/selenium/blob/trunk/java/CHANGELOG for which cdp version is supported by the used (currently: 4.8.1) selenium version
RUN CHROMEDRIVER_VERSION="110.0.5481.77" \
    && wget --no-verbose -O /tmp/chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
    && rm -rf /opt/chromedriver \
    && unzip /tmp/chromedriver_linux64.zip -d /opt \
    && rm /tmp/chromedriver_linux64.zip \
    && mv /opt/chromedriver /opt/chromedriver-$CHROMEDRIVER_VERSION \
    && chmod 755 /opt/chromedriver-$CHROMEDRIVER_VERSION \
    && ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION /usr/bin/chromedriver

RUN apt-get update && apt-get install -y firefox-esr
RUN apt-get install -y default-jre default-jdk
 
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.32.2/geckodriver-v0.32.2-linux64.tar.gz \
    && tar -xvzf geckodriver-v0.32.2-linux64.tar.gz \
    && rm geckodriver-v0.32.2-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/geckodriver

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY domainer.py /

CMD ["python3", "/domainer.py"]