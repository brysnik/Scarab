#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> String {
    match run_python() {
        Ok(msg) => msg,
        Err(_) => "Error running Python code".to_string()
    }
}

#[post("/create_venv/<name>")]
fn post_venv(name: &str) -> String {
    match create_venv(name) {
        Ok(msg) => msg,
        Err(_) => "Error creating venv".to_string()
    }
}

#[launch]
fn rocket() -> _ {
    rocket::build()
    .mount("/", routes![index])
    .mount("/", routes![post_venv])
}

use pyo3::Python;
use pyo3::PyResult;
use pyo3::prelude::*;
use pyo3::types::IntoPyDict;

fn run_python() -> PyResult<String> {
    Python::with_gil(|py| {
        let sys = py.import("sys")?;
        let os = py.import("os")?;
        let version: String = sys.getattr("version")?.extract()?;
        let user: String = os.getattr("getlogin")?.call0()?.extract()?;
        Ok(format!("Hello {}, I'm Python {}", user, version))
    })
}


fn create_venv(name: &str) -> PyResult<String> {
    Python::with_gil(|py| {
        let venv = py.import("venv")?;
        let kwargs = [("with_pip", true)].into_py_dict(py)?;
        venv.getattr("create")?.call((name, ), Some(&kwargs))?;
        Ok(format!("venv created successfully"))
    })
}
