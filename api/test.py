from censys.search import CensysIPv4

c = CensysIPv4()

for page in c.search(
    "443.https.get.headers.server: Apache AND location.country: Japan",
    max_records=10
):
    print(page)

# You can optionally restrict the (resource-specific) fields to be
# returned in the matching results. Default behavior is to return a map
# including `location` and `protocol`.
fields = [
    "ip",
    "updated_at",
    "443.https.get.title",
    "443.https.get.headers.server",
    "443.https.get.headers.x_powered_by",
    "443.https.get.metadata.description",
    "443.https.tls.certificate.parsed.subject_dn",
    "443.https.tls.certificate.parsed.names",
    "443.https.tls.certificate.parsed.subject.common_name",
]

for page in c.search(
        "443.https.get.headers.server: Apache AND location.country: Japan",
        fields,
        max_records=10,
    ):
    print(page)
