# call the runtime for the image, use alpine for lower runtime image
FROM python3:12-alpine

# the directory where the build would be kept in the container
WORKDIR /app

# copy your dependencies
COPY requirements.txt .

# install the dependencies
RUN pip install  --no-cached-dir -r requirements.txt

# copy the host app to the container
COPY . .

ARG version

ENV VERSION=$version

#for documentation to know the port that the app is runing on on the conatiner
EXPOSE 5000

# Run the app
CMD ["gunicorn", "auth_service:app"]

