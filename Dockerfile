#一═デ⭕️_𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫_⭕️デ═一
FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
#一═デ⭕️_𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫_⭕️デ═一
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/mentiontard/tele-ytm.git
RUN cd tele-ytm
#一═デ⭕️_𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫_⭕️デ═一
WORKDIR /tele-ytm
RUN pip install -r meow.txt
CMD python3 BOOTUP.py
#一═デ⭕️_𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐌𝐮𝐬𝐢𝐜 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫_⭕️デ═一
