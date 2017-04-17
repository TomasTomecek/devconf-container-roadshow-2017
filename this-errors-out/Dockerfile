FROM fedora:25
COPY ./target/release/this-errors-out /
# TODO: create common base image with dnf cache
RUN adduser -m -u 1000 worker && dnf makecache  # so we have cache during workshop
ENTRYPOINT ["/this-errors-out"]
CMD [""]
USER 1000
