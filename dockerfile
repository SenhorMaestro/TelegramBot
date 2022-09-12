FROM python:slim
ENV TOKEN='YourTOKEN'
COPY . .
RUN pip install -r req.txt
CMD python bot.py