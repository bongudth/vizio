class Completion:
    @staticmethod
    def create(
        prompt: str,
        page: int = 1,
        count: int = 10,
        safe_search: str = "Moderate",
        on_shopping_page: bool = False,
        mkt: str = "",
        response_filter: str = "WebPages,Translations,TimeZone,Computation,RelatedSearches",
        domain: str = "youchat",
        query_trace_id: str = None,
        chat: list = None,
        include_links: bool = False,
        detailed: bool = False,
        debug: bool = False,
        proxy: Optional[str] = None,
    ) -> PoeResponse:
        if chat is None:
            chat = []

        proxies = (
            {"http": "http://" + proxy, "https": "http://" + proxy} if proxy else {}
        )

        client = Session(client_identifier="chrome_108")
        client.headers = Completion.__get_headers()
        client.proxies = proxies

        response = client.get(
            f"https://you.com/api/streamingSearch",
            params={
                "q": prompt,
                "page": page,
                "count": count,
                "safeSearch": safe_search,
                "onShoppingPage": on_shopping_page,
                "mkt": mkt,
                "responseFilter": response_filter,
                "domain": domain,
                "queryTraceId": str(uuid4())
                if query_trace_id is None
                else query_trace_id,
                "chat": str(chat),  # {'question':'','answer':' ''}
            },
        )

        if debug:
            print("\n\n------------------\n\n")
            print(response.text)
            print("\n\n------------------\n\n")

        if "youChatToken" not in response.text:
            return Completion.__get_failure_response()

        you_chat_serp_results = re.search(
            r"(?<=event: youChatSerpResults\ndata:)(.*\n)*?(?=event: )", response.text
        ).group()
        third_party_search_results = re.search(
            r"(?<=event: thirdPartySearchResults\ndata:)(.*\n)*?(?=event: )",
            response.text,
        ).group()
        # slots                   = findall(r"slots\ndata: (.*)\n\nevent", response.text)[0]

        text = "".join(re.findall(r"{\"youChatToken\": \"(.*?)\"}", response.text))

        extra = {
            "youChatSerpResults": json.loads(you_chat_serp_results),
            # 'slots'                   : loads(slots)
        }

        response = PoeResponse(
            text=text.replace("\\n", "\n").replace("\\\\", "\\").replace('\\"', '"')
        )
        if include_links:
            response.links = json.loads(third_party_search_results)["search"][
                "third_party_search_results"
            ]

        if detailed:
            response.extra = extra
