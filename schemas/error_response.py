from pydantic import BaseModel


class HTTPErrorSchema(BaseModel):
    detail: str
    status_code: int

error_responses ={
    401:{
        "model":HTTPErrorSchema,
        "description": "desautorizado"
    },
    401:{
        "model":HTTPErrorSchema,
        "description": "Not Found"
    }
}

