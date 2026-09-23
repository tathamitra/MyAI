def build_context(results):

    context_parts = []

    for result in results:
        context_parts.append(result["chunk"])

    return "\n\n".join(context_parts)
